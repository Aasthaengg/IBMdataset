m,k = map(int,input().split())
if k == 0:
    l = [i // 2 for i in range(2 ** (m + 1))]
    print(*l)
    exit()

if m == 0:
    if k == 0:
        print(0, 0)
    else:
        print(-1)
    exit()

if m == 1:
    if k == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
    exit()

if not 0 <= k < 2 ** m:
    print(-1)
    exit()

l = [0]
for i in range(2 ** (m - 1) - 1):
    l.append(2 ** (m - 1) - i)
for i in range(2 ** (m - 1)):
    l.append(i + 1)
for i in range(2 ** m):
    if i == 0:
        l.append(0)
    elif i == 2 ** (m - 1):
        l.append(l[i])
    else:
        l.append(l[i] + 2 ** (m - 1) - 1)

if k == 1:
    print(*l)
    exit()

for i in range(len(l)):
    if l[i] == 1:
        l[i] = k
    elif l[i] == k:
        l[i] = 1
print(*l)