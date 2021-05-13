n = int(input())
ls = list(map(int, input().split()))

cnt = 0

for i in range(n):
    if i == ls[ls[i] - 1] - 1:
        cnt += 1

print(int(cnt * 0.5))