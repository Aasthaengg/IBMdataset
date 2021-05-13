a, b = map(int, input().split())
ans = "Odd" if a * b % 2 == 1 else "Even"
print(ans)
