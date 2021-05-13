n = int(input())
A = list(int(input()) for _ in range(n))

cnt = 0
num = 1

for i in range(n):
    num = A[num - 1]
    cnt += 1
    if num == 2:
        print(cnt)
        exit()
print(-1)