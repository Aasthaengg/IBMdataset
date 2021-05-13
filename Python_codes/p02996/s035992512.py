n = int(input())
ab = [[] for _ in range(n)]
for i in range(n):
    ab[i] = list(map(int, input().split()))
ab.sort(key=lambda x: x[1])
r = 0
flag = True
for a, b in ab:
    r += a
    if r > b:
        flag = False
        break

print("Yes") if flag else print("No")
