n = int(input())
d, x = map(int, input().split())
A = list(int(input()) for _ in range(n))

cnt = 0
for a in A:
    tmp = (d - 1) // a
    cnt += tmp + 1

print(cnt + x)
