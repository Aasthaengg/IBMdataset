c = [input() for i in range(2)]
for i in range(3):
    if c[0][i] != c[1][2-i]:
        print("NO")
        exit()
print("YES")