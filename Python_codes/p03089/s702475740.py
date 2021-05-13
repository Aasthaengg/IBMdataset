n = int(input())
b = list(map(int, input().split()))
ans = []
for i in range(n, 0, -1):
    ok = False
    for j in range(i, 0, -1):
        if b[j - 1] == j:
            ans.append(b.pop(j - 1))
            ok = True
            break
    if not ok:
        print(-1)
        exit()

for i in range(n):
    print(ans.pop())
