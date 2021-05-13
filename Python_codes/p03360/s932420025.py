x = list(map(int, input().split()))
k = int(input())
ans = sum(x) - max(x)
ans += max(x) * 2 ** k
print(ans)
