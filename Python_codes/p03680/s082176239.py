N = int(input())
li = [int(input()) for _ in range(N)]
i = 1
for n in range(N):
    i = li[i-1]
    if i == 2:
        print(n+1)
        break
else:print(-1)