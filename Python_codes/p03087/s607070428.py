# C - GeT AC
N,Q = map(int,input().split())
S = input()
L = []
R = []
for _ in range(Q):
    l,r = map(int,input().split())
    l -= 1;r -= 1
    L.append(l)
    R.append(r)

# 右隣に 'C' が存在する 'A' の個数をカウント
cnt = [0]*N
for i in range(N-1):
    if S[i] == 'A' and S[i+1] == 'C':
        cnt[i] = 1

# s[i]: i 番目までに出てくる右隣に 'C' が存在する 'A' の個数
s = [0]*(N+1)
for i in range(N):
    s[i+1] = s[i] + cnt[i]

for l,r in zip(L,R):
    ans = s[r] - s[l]
    print(ans)