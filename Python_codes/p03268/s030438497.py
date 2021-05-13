import math
n, k = map(int, input().split())

if k == 1:
    print(n**3)
    exit()
if n == 1:
    print(1*(k==3))
    exit()
    
ans = 0
for i in range(n):
    a = i+1
    if 2*(i+1) % k == 0:
        lb = math.floor((a%k)/k)
        if a%k == 0:
            lb = 1
        ub = math.floor((n-a%k)/k)
        # print(a, (a%k)/k, (n-a%k)/k)
        ans += (ub-lb+1)**2
print(ans)
