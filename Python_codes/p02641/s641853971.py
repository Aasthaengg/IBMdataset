x,n=map(int,input().split())
p=list(map(int,input().split()))

ans=0
for i in range(102):
    if not i in p and abs(x-ans)>abs(x-i):
        ans=i
print(ans)