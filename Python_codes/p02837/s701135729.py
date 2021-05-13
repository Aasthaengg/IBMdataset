n = int(input())
lst = []
for i in range(n):
    a = int(input())
    b = []
    for j in range(a):
        x, y = map(int,input().split())
        x -= 1
        b.append([x, y])
    lst.append(b)
ans = 0

for i in range(2**n):
    honest = []
    contradiction_f = False

    for j in range(n):
        if i>>j & 1:
            honest.append(j)

    for j in honest:
        judge = lst[j]
        for k in judge:
            if k[1] == 1:
                if not k[0] in honest:
                    contradiction_f = True
                    break
            else:
                if k[0] in honest:
                    contradiction_f = True
                    break

    if not contradiction_f:
        ans = max(ans, len(honest))

print(ans)