X, N = map(int, input().split())
L = list(map(int, input().split()))

if len(L) == 0:
    print(X)
    exit()

list = [0 for _ in range(len(L))]
for i in range(len(L)):
    list[i] = abs(X - L[i])
list = sorted(list)

if min(list) != 0:
    print(X)
    exit()
else:
    num = 1
    cnt = 0
    for i in range(1, len(list)):
        if list[i] != num:
            break
        cnt += 1
        if cnt == 2:
            cnt = 0
            num += 1
if cnt == 0:
    print(X - num)
else:
    if X + num in L:
        print(X - num)
    else:
        print(X + num)
