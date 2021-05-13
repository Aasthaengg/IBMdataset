s, t = [input() for _ in range(2)]
print("Yes" if "".join(sorted(s)) < "".join(sorted(t, reverse=True)) else "No")