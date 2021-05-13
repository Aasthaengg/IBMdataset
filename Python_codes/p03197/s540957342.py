n = int(input())
a = list(int(input()) for _ in range(n))

cnt = 0
for i in range(n):
    if a[i] % 2 == 0:
        cnt += 1

if cnt == n:
    print("second")
else:
    print("first")