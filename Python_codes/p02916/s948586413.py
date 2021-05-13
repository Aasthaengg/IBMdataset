n=int(input())
a=list(map(int,input().split()))
b=[0]+list(map(int,input().split()))
c=[0]+list(map(int,input().split()))

cnt=0
before=0

for i in range(n):
    cnt+=b[a[i]]
    if a[i]==before+1:
        cnt+=c[before]
    before=a[i]
print(cnt)