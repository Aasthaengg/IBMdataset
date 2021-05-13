N = int(input())
ls = list(map(int,input().split()))
ans=0
n=0
nls = []
for i in range(N-1):
    if ls[i] >= ls[i+1]:
        n += 1 
    elif ls[i] < ls[i+1]:
        ans = max(ans,n)
        n = 0
    
    if i==N-2:
        ans = max(ans,n)

print(ans)