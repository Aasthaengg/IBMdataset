a, b = map(int, input().split())
ans = a - b * 2
ans = ans if ans > 0 else 0
print(ans)