C = [input() for _ in range(2)]
for i in range(3):
    if C[0][i] != C[1][2-i]:
        print("NO")
        break
else: print("YES")