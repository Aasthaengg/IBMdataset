N = int(input())
ans = 0
for i in range(1,N+1):
    if i*i>N:break
    if N%i==0:
        ans += N//i-1 if N//i-1>i else 0
print(ans)