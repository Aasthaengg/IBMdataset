N, X = map(int, input().split())
L = list(map(int, input().split()))

curr_bounce = 0
cnt = 1
for i in range(N):
    curr_bounce += L[i]
    if curr_bounce > X:
        break
    else:
        cnt += 1
print(cnt)