s, t = list(input() for i in range(2))
print("Yes" if sorted(s) < sorted(t)[::-1] else "No")