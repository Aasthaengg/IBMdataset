N, K = map(int,input().split())

win = 0
for i in range(1,N+1):
    n = 0
    point = i
    while point < K:
        point *= 2
        n += 1
    win += (1/N)*(0.5**n)

print(win)