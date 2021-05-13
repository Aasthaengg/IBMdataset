N = int(input())
H = list(map(int, input().split()))

H = [0] + H
cnt = 0
for i in range(1, N + 1):
    cnt += max(H[i] - H[i - 1], 0)


print(cnt)