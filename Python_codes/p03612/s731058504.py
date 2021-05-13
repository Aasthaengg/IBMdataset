N = int(input())
p = list(map(int, input().split()))
p = [i - 1 for i in p]

cnt = 0
for i in range(N):
    if i == N - 1 and p[i] == i:
        p[i], p[i-1] = p[i-1], p[i]
        cnt += 1
    elif p[i] == i:
        p[i], p[i+1] = p[i+1], p[i]
        cnt += 1

print(cnt)
