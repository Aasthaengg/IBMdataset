N = int(input())
b = list(map(int, input().split()))

ans = []

for i in range(N):
    L = -1
    for j in range(len(b)):
        if j+1 == b[j]:
            L = j

    if L != -1:
        ansi = b.pop(L)
        ans.append(ansi)

if len(ans) != N:
    print(-1)
else:
    ans = list(reversed(ans))
    for a in ans:
        print(a)
