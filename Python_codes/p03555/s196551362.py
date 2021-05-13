C=[input() for _ in range(2)]
for i in range(3):
    if C[0][i]==C[1][-(i+1)]:
        continue
    else:
        print("NO")
        exit()
print("YES")