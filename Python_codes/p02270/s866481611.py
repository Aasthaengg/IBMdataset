import sys
n,k = map(int,input().split())
input = sys.stdin.readline
W = [int(input()) for i in range(n)]
l = max(W)-1
W.append(10**13)
h = sum(W)
while l+1 < h:
    ok = (l+h)//2
    track = 0
    cur = 0
    for i in range(n+1):
        cur += W[i]
        if cur > ok:
            track += 1
            cur = W[i]
        elif cur == ok:
            if i != n-1:
                track += 1
                cur = 0
    if track > k:
        l = ok
    else:
        h = ok
print(h)
