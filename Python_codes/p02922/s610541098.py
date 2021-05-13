a, b = map(int, input().split())
ans = (((b-1)-1) // (a-1) + 1) if b > 1 else 0
print(ans)