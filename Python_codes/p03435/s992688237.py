import sys
c = [[int(x) for x in input().split()] for _ in range(3)]

for i in range(2):
    for j in range(2):
        if c[j][i + 1] - c[j][i] != c[j + 1][i + 1] - c[j + 1][i]:
            print("No")
            sys.exit()
print("Yes")