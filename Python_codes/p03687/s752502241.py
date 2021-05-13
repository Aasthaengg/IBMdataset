s = input()
def simulate(c):
    W = list(s[:])
    cnt = 0
    while len(set(W)) > 1:
        for i,w in enumerate(W):
            if w==c and i >= 1:
                W[i-1] = c
        cnt += 1
        W.pop()
    return cnt

ans = len(s)
for c in set(s):
    ans = min(ans, simulate(c))

print(ans)