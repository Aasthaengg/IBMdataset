S = input().rstrip()
T = input().rstrip()

ans = 1000
for offset in range(len(S) - len(T) + 1):
    miss = 0
    for s, t in zip(S[offset:offset+len(T)], T):
        if s != t:
            miss += 1
    ans = min(ans, miss)

print(ans)