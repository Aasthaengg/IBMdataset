n,k = list(map(int, input().split()))
ans = 0
sum_n = (n+1)*n/2

for i in range(k, n+2):
    tmp_b = (i)*(i-1)/2
    tmp_a = sum_n - (n-i+1)*(n-i)/2
    ans += tmp_a - tmp_b + 1
print(int(ans)%(10**9+7))
