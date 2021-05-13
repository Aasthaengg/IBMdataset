A, B = map(int, input().split())
k = 50
d = [["." if i < k else "#" for j in range(2 * k)] for i in range(2 * k)]
A -= 1
B -= 1
for i in range(0, 50, 2):
    for j in range(0, 100, 2):
        if B > 0:
            d[i][j] = "#"
            B -= 1

for i in range(51, 100, 2):
    for j in range(0, 100, 2):
        if A > 0:
            d[i][j] = "."
            A -= 1

print(2 * k, 2 * k)
for s in d:
    print("".join(s))
