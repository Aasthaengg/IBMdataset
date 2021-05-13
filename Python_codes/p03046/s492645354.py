m, k = map(int, input().split())

if k >= 2**m:
    print(-1)
    exit()

if m == 0:
    print(0, 0)
    exit()
if m == 1:
    if k == 0:
        print(0, 0, 1, 1)
        exit()
    else:
        print(-1)
        exit()

A = [k]
for i in range(2**m):
    if i == k:
        continue
    A.append(i)
A.append(k)
for i in range(2**m - 1, -1, -1):
    if i == k:
        continue
    A.append(i)

print(*A)
