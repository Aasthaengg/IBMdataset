N = int(input())
S1 = list(input())
S2 = list(input())
ans = 1
MOD = 1000000007
flag_1 = False

if S1[0] == S2[0]:
    ans *= 3
    flag = 'X'
else:
    ans *= 6
    flag = 'Y'

for i in range(1,N):
    if i == 1 and flag == 'Y':
        continue
    if flag_1:
        flag_1 = False
        continue
    if S1[i] == S2[i]:
        if flag == 'X':
            ans *= 2
        else:
            flag = 'X'
    else:
        if flag == 'X':
            ans *= 2
            flag = 'Y'
        else:
            ans *= 3
        flag_1 = True
    ans %= MOD
print(ans)
