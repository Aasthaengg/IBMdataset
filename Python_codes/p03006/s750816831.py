N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i],y[i] = map(int,input().split())

if N == 1:
    print(1)
else:
    memo = {}

    for i in range(N-1):
        for j in range(i+1,N):
            dx = x[j] - x[i]
            dy = y[j] - y[i]
            if (dx,dy) in memo:
                memo[(dx,dy)] += 1
            elif (-dx,-dy) in memo:
                memo[(-dx,-dy)] += 1
            else:
               memo[(dx,dy)] = 1
            #print(memo)

    M = max(memo.values())

    print(N-M)
