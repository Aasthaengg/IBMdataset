a, b = map(int, input().split())
ans = "Possible" if a*b*(a+b) % 3 == 0 else "Impossible"
print(ans)