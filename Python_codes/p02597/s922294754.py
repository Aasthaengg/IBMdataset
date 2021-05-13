n = int(input())
c = list(input())
wcount = [0] * n
rcount = [0] * n
for i in range(n):
    if c[i] == 'W':
        wcount[i] = 1
    if c[-(i+1)] == 'R':
        rcount[-(i+1)] = 1
    if i != 0:
        wcount[i] = wcount[i] + wcount[i-1]
        rcount[-(i+1)] = rcount[-(i+1)] + rcount[-i]
ans = n
for i in range(n+1):
    if i == 0:
        W = 0
        R = rcount[0]
    elif i == n:
        W = wcount[-1]
        R = 0
    else:
        W = wcount[i-1]
        R = rcount[i]
    tmp = max(W, R)
    if tmp < ans:
        ans = tmp
print(ans)