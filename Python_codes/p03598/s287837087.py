N = int(input())
K = int(input())
x = list(map(int,input().split()))
ans = 0
for i in range(N):
    if(x[i] >= abs(x[i]-K)):
        ans += 2*abs(x[i]-K)
    else:
        ans += 2*x[i]
print(ans)