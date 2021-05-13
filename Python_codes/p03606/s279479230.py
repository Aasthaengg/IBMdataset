N = int(input())

cnt = 0
for l in range(N):
    a, b = [int(i) for i in input().split()]
    cnt += abs(b-a) + 1

print(cnt)