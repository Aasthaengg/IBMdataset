h, w = map(int, input().split())
S = [[] for _ in range(h)]
for i in range(h):
    S[i] = list(input())

ans = 0
L = [[0]*w for _ in range(h)]
for hi in range(h):
    cnt = 1
    for wi in range(w):
        if S[hi][wi]=='#':
            L[hi][wi] = 0
            cnt = 1
        else:
            L[hi][wi] = cnt
            cnt += 1

R = [[0]*w for _ in range(h)]
for hi in range(h):
    cnt = 1
    for wi in range(w):
        if S[hi][w-wi-1]=='#':
            R[hi][w-wi-1] = 0
            cnt = 1
        else:
            R[hi][w-wi-1] = cnt
            cnt += 1

D = [[0]*w for _ in range(h)]
for wi in range(w):
    cnt = 1
    for hi in range(h):
        if S[hi][wi]=='#':
            D[hi][wi] = 0
            cnt = 1
        else:
            D[hi][wi] = cnt
            cnt += 1

U = [[0]*w for _ in range(h)]
for wi in range(w):
    cnt = 1
    for hi in range(h):
        if S[h-hi-1][wi] == '#':
            U[h-hi-1][wi] = 0
            cnt = 1
        else:
            U[h-hi-1][wi] = cnt
            cnt += 1

ans = 0
for hi in range(h):
    for wi in range(w):
        ans = max(ans, L[hi][wi]+R[hi][wi]+D[hi][wi]+U[hi][wi]-3)
print(ans)