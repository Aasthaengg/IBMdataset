import sys
input = sys.stdin.readline
mod = 1000000007

N = int(input())
S1 = input().rstrip()
S2 = input().rstrip()

# 探索済みかどうかの管理
s = set()

# 答え
ans = 1

if S1[0] == S2[0]:
    ans *= 3
    ans %= mod
    s.add(S1[0])
else:
    ans *= 3 * 2
    ans %= mod
    s.add(S1[0])
    s.add(S2[0])

for i in range(1, N):
    # タテ
    if S1[i] == S2[i]:
        if S1[i - 1] == S2[i - 1]:
            ans *= 2
            ans %= mod
        s.add(S1[i])
    
    # ヨコ
    elif S1[i] not in s and S1[i - 1] == S2[i - 1]:
        ans *= 2
        ans %= mod
        s.add(S1[i])
        s.add(S2[i])
    elif S1[i] not in s:
        ans *= 3
        ans %= mod
        s.add(S1[i])
        s.add(S2[i])

print(ans)