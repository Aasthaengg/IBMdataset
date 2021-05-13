n=int(input())
c=list(map(int, input().split()))
ans=0
f=0

for i in range(n):
    if c[i]%2!=0:
        print(0)
        exit()

while f==0:
    for i in range(n):
        c[i]=c[i]/2
        if c[i]%2!=0:
            ans+=1
            print(ans)
            exit()
    ans+=1