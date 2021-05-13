L, R = list(map(int,input().split()))

if(R - L) >= 2019:
    print(0)
    exit()
 
ans = float('inf')
for i in range(L, R):
    for j in range(i+1, R+1):
        t = i*j%2019
        ans = min(ans,t)
print(ans)