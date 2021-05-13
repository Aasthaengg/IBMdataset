N = int(input())
cnt = 0

for a in range(1, N):
    cnt += int((N - 1) / a)

print(cnt)