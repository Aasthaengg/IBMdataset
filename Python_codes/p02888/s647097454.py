from bisect import bisect_left
N=int(input())
triangle=[]
count=0
L=list(map(int,input().split()))
L.sort()
#print(L)
for a in range(N):
    for b in range(a+1,N):
        c=L[a]+L[b]
        zahyo=bisect_left(L,c)
        count+=max(0,zahyo-b-1)
print(count)
