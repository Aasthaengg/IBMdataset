N = int(input())
S = [list(input()) for i in range(2)]
i = 0
ans = 1
mod = 10**9+7
if S[0][i]==S[1][i]:
    ans = 3
    i += 1
    flag = 0
else:
    ans = 6
    i += 2
    flag = 1
while i<N:
    if flag==0 and S[0][i]==S[1][i]:
        ans *= 2
        ans %= mod
        i += 1
        flag = 0
    elif flag == 1 and S[0][i]==S[1][i]:
        i += 1
        flag = 0
    elif flag == 0 and S[0][i]!=S[1][i]:
        ans *= 2
        ans %= mod
        i += 2
        flag = 1
    else:
        ans *= 3
        ans %= mod
        i += 2
        flag = 1
print(ans)
