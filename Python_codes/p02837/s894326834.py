n = int(input())
all = 1<<n
statement = []
for i in range(n):
    A = int(input())
    statement.append([])
    for j in range(A):
        x, y = map(int, input().split())
        statement[i].append([x-1, y])
ans = 0
for i in range(all):
    ok = True
    num = 0
    for j in range(n):
        if i & 1<<j:
            num += 1
            for s in statement[j]:
                if (i & 1<<s[0]) != (s[1]<<s[0]):
                    ok = False
    if ok:
        ans = max(ans, num)
print(ans)
