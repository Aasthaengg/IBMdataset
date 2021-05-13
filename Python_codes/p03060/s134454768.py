n=int(input())
v=list(map(int,input().split()))
c=list(map(int,input().split()))
k=0
for i in range(n):
    a=v[i]-c[i]
    if a>=0:
        k+=a
print(k)


