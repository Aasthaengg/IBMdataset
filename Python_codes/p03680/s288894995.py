n = int(input())
A = []

for _ in range(n):
    A.append(int(input()))

now = 0
cnt = 0
for i in range(n):
    if now == 1:
        print(cnt)
        exit()
    cnt += 1
    now = A[now] - 1

print(-1)
