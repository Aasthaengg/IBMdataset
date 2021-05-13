n,m,x=map(int, input().split())
a=list(map(int,input().split()))
ans1 = 0
ans2 = 0
for i in range(x-1,-1,-1):
    if i+1 in a:
        ans1 += 1 
for j in range(x-1,n):
    if j+1 in a:
        ans2 += 1
print(min(ans1,ans2))