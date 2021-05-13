n=int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
be = list()
ab = list()
for i in range(n):
    j,k=a[i],b[i]
    if j<k:
        be.append(k-j)
    elif j>k:
        ab.append(j-k)
p=len(be)
be=sum(be)
ab.sort(reverse=True)
k=0
if be==0:
    print(0)
    exit()
for i in range(len(ab)):
    k+=ab[i]
    if k >= be:
        print(p+i+1)
        exit()
print(-1)