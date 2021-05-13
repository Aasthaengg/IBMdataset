import sys
n,m = map(int, input().split())

# it watches only end of union
# for i in range(m):
#     l,r,d = map(int, input().split())
#     if ml[l] == -1 and ml[r] == -1:
#         ml[l] = 0
#         ml[r] = d
#     elif ml[l] != -1 and ml[r] == -1:
#         ml[r] = d + ml[l]
#         if ml[r] > n:
#             print('R', i, ml[l], ml[r], flush=True)
#             print('No', flush=True)
#             sys.exit()
#     elif ml[l] == -1 and ml[r] != -1:
#         ml[l] = ml[r] - d
#         if ml[l] < 1:
#             print('L', i, ml[l], ml[r], flush=True)
#             print('No', flush=True)
#             sys.exit()
#     else:
#         if ml[r] - ml[l] != d:
#             print('B', i, l, ml[l], r, ml[r], d, flush=True)
#             print('No', flush=True)
#             sys.exit()
# print('Yes', flush=True)

class UnionfindWithWeight():
    def __init__(self,n):
        self.parents=[-1]*n
        self.ranks=[0]*n
        self.dist=[0]*n
    def find(self,x):
        if self.parents[x]<0:
            return self.dist[x],x
        else:
            tmp=self.find(self.parents[x])
            self.dist[x]+=tmp[0]
            self.parents[x]=tmp[1]
            return self.dist[x],self.parents[x]
    def union(self,x,y,d):
        rx=self.find(x)[-1]
        ry=self.find(y)[-1]
        diff=d+self.dist[x]-self.dist[y]
        if rx==ry:
            if diff!=0:
                return True
            return False
        if self.ranks[ry]>self.ranks[rx]:
            rx,ry=ry,rx
            diff=-diff
        self.parents[ry]=rx
        self.dist[ry]=diff
        if self.ranks[ry]==self.ranks[rx]:
            self.ranks[rx]+=1
        return False
lrd = []
for i in range(m):
    l,r,d = list(map(int, input().split()))
    lrd.append([l,r,d])
v=UnionfindWithWeight(n)
for i in lrd:
    l, r, d = i
    if v.union(l-1,r-1,d):
        print('No')
        import sys
        sys.exit()
print('Yes')
