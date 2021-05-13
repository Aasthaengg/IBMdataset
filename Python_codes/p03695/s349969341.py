N=int(input())
a=list(map(int,input().split()))
for i in range(N):
    a[i]//=400

ans=0
for i in range(8):
    if i in a:
        ans+=1
y=0
for x in a:
    if x>=8:
        y+=1
print(max(ans,1),ans+y)
