N, K = map(int, input().split())
S = input().rstrip()

cnt = 0
s0 = "$"
for s in S:
    if s != s0:
        cnt += 1
    s0 = s

print(min(N-cnt+2*K,N-1))