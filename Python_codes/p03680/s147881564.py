N = int(input())
a = [int(input()) for _ in range(N)]

count = 0
i = 1
for _ in range(N):
    i = a[i-1]
    count += 1
    if i == 2:
        print(count)
        break
else:
    print(-1)