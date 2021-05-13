c = [input() for _ in range(2)]
tmp = c[0][0] == c[1][2] and c[0][1] == c[1][1] and c[0][2] == c[1][0]
print("YES" if tmp else "NO")