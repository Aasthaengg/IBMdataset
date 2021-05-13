n, m = map(int, input().split())
a = [""] * n
b = [""] * m

for i in range(n):
    a[i] = input()

for i in range(m):
    b[i] = input()

for i in range(n):
    for j in range(n):
        if i + m > n or j + m > n:
            continue
        flag = True
        for k in range(m):
            for l in range(m):
                if a[i + k][j + l] != b[k][l]:
                    flag = False
        if flag is True:
            print("Yes")
            exit(0)

print("No")
