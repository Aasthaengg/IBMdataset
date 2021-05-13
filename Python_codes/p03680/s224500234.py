N = int(input())
a = [int(input()) for _ in range(N)]
num = 1
cnt = 0
for i in range(200000):
    num = a[num-1]
    cnt += 1
    if num == 2:
        print(cnt)
        exit()
print(-1)