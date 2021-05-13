N = int(input())
B = list(map(int, input().split()))

res = []
for i in range(N):
    for j in range(N-i-1, -1, -1):
        if B[j] == j+1:
            res.append(j+1)
            B = B[:j]+B[j+1:]
            break
    else:
        break

if len(res) == N:
    res.reverse()
    for r in res:
        print(r)
else:
    print(-1)