m, k= map(int, input().split())

if 2**m <= k:
    print(-1)
    exit()

if m == 1:
    if k == 0:
        print("0 0 1 1")
    if k == 1:
        print(-1)
    exit()

li = []
for i in range(2**m):
    if i != k:
        li.append(i)
li = li + [k] + list(reversed(li)) + [k]
print(" ".join(map(str, li)))