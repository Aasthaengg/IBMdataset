N = int(input())
b = list(map(int, input().split()))

ans = []
fault = False
for _ in range(N):
    for cursol in range(len(b) - 1, -1, -1):
        if b[cursol] == cursol + 1:
            ans.append(b.pop(cursol))
            break
    else:
        fault = True
if fault:
    print(-1)
else:
    ans.reverse()
    for el in ans:
        print(el)