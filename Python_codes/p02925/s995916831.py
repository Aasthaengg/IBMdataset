import sys
from collections import deque
input = sys.stdin.readline
def combination_to_index(a,b,n):
    if(b<a):
        a,b = b,a
    return (2*n-a)*(a-1)//2+b-a

def main():
    N = int(input())
    M = N*(N-1)//2
    gp = [[] for _ in range(M+1)]
    cnts = [0]*(M+1)
    for a in range(1,N+1):
        A = [int(x) for x in input().split()]
        for ind,b in enumerate(A[:-1]):
            fr = combination_to_index(a,b,N)
            to = combination_to_index(a,A[ind+1],N)
            gp[fr].append(to)
            cnts[to] += 1

    for ind,i in enumerate(cnts):
        if(i==0 and ind!=0):
            gp[0].append(ind)
            cnts[ind]+=1

    ans = 0
    cnt = 0
    stk = deque()
    stk.append((0,0))
    while stk:
        n,ans = stk.popleft()
        for x in gp[n]:
            cnts[x]-=1
            if(cnts[x]==0):
                stk.append((x,ans+1))
                cnt += 1
    if(cnt!=M):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
