N = int(input())
S = list(input())

ans = 10**9

T = "#."
W = '.'
B = '#'

dp_blk = [0]*(N+1)
dp_wht = [0]*(N+1)

if all([B==c for c in S]) or all([W==c for c in S]):
    print(0)
    exit(0)

for ix in range(N):
    if S[ix] == B:
        dp_blk[ix+1] += dp_blk[ix] + 1
        dp_wht[ix+1] += dp_wht[ix]
    else:
        dp_wht[ix+1] += dp_wht[ix] + 1
        dp_blk[ix+1] = dp_blk[ix]

# print("dp_blk", dp_blk)
# print("dp_wht", dp_wht)

for lix in range(N+1):
    b_flip = dp_blk[lix]
    w_flip = dp_wht[N] - dp_wht[lix]
    flip = b_flip + w_flip
    # print(lix, flip)
    if ans > flip:
        ans = flip

# ab = N - dp_blk[N]
# aw = N - dp_wht[N]
# ans = min(ab, aw, ans)
    
print(ans)