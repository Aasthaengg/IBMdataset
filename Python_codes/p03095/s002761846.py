N = int(input())
S = input()

mod = 10**9+7

dic = {}
for i in range(N):
    if S[i] in dic:
        dic[S[i]] += 1
    else:
        dic[S[i]] = 1

ans = 1
for key in dic:
    ans *= dic[key]+1
    ans %= mod

ans -= 1
print(ans)