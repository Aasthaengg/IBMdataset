a, b, c, d = map(int, input().split())
ans = "Left" if a+b > c+d else "Balanced" if a+b == c+d else "Right"
print(ans)