class SegmentTreeDual():
    def __init__(self,arr,op=lambda x,y:y if y != -1 else x,ie=-1):
        self.h = (len(arr)-1).bit_length()
        self.n = 2**self.h
        self.ie = ie
        self.op = op
        self.val = [ie for _ in range(self.n)]
        self.laz = [ie for _ in range(2*self.n)]
        for i in range(len(arr)):
            self.val[i] = arr[i]

    def propagate(self,k):
        if self.laz[k] == self.ie: return
        if self.n <= k:
            self.val[k-self.n] = self.op(self.val[k-self.n],self.laz[k])
            self.laz[k] = self.ie
        else:
            self.laz[2*k] = self.op(self.laz[2*k],self.laz[k])
            self.laz[2*k+1] = self.op(self.laz[2*k+1],self.laz[k])
            self.laz[k] = self.ie

    def update(self,left,right,x):
        left += self.n
        right += self.n
        #可換なら不要?
        for i in range(self.h)[::-1]:
            self.propagate(left>>i)
            self.propagate(right>>i)
        #
        while right-left>0:
            if right & 1:
                right -= 1
                self.laz[right] = self.op(self.laz[right],x)
            if left & 1:
                self.laz[left] = self.op(self.laz[left],x)
                left += 1
            left >>= 1
            right >>= 1
    def get(self,index):
        res = self.val[index]
        index += self.n
        while index>0:
            res = self.op(res,self.laz[index])
            index //= 2
        return res


from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline
INF = 10**18

N,Q = map(int,input().split())
P = [-INF,INF]
R = []

for i in range(N):
    s,t,x = map(int,input().split())
    R.append((s-x,t-x,x))
    P.append(s-x)
    P.append(t-x)
D = []
for i in range(Q):
    d = int(input())
    D.append(d)
    P.append(d)

R = sorted(R,key=lambda x:x[2],reverse=True)
P = sorted(set(P))
S = dict()
for i in range(len(P)):
    S[P[i]] = i

st = SegmentTreeDual(
                    arr = [-1 for _ in range(len(P))],
                    op = lambda x,y:y if y != -1 else x,
                    ie = -1
                    )
for i in range(N):
    st.update(S[R[i][0]],S[R[i][1]],R[i][2])

ans = []

for i in range(Q):
    ans.append(st.get(S[D[i]]))

print('\n'.join(map(str,ans)))