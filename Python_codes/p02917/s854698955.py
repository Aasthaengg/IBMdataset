n = int(input())
B = tuple(map(int, input().split()))

ans = B[0]
for i in range(1, n-1):
    ans += min(B[i-1], B[i])
print(ans+B[-1])
