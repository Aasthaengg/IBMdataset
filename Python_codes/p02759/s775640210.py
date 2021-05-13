N = int(input())
ans = N // 2
ans += 1 if N % 2 != 0 else 0
print(ans)