N = int(input())
a = tuple(map(int, input().split()))
b = [-1] * N
for i in range(N//2, N):
    b[i] = 1 if a[i] == 1 else 0
for j in range(N//2-1, -1, -1):
    acc = sum([b[i] for i in range(2*j+1, N, j+1)])
    if a[j] == 1 and acc % 2 == 0:
        b[j] = 1
    elif a[j] == 0 and acc % 2 != 0:
        b[j] = 1
    elif a[j] == 0 and acc % 2 == 0:
        b[j] = 0
    elif a[j] == 1 and acc % 2 != 0:
        b[j] = 0
if -1 in b:
    print(-1)
    exit()
ans = len([i for i in b if i == 1])
print(ans)
if ans == 0:
    exit()
print(*[j+1 for j, v in enumerate(b) if v == 1])