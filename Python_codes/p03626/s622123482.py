MOD = 10**9 + 7
N = int(input())
S = input()
S2 = input()
check = []
flg = False
for i in range(N-1):
    if flg:
        check.append(2)
        flg = False
        continue
    if S[i] == S[i+1]:
        flg = True
    else:
        check.append(1)
if flg:
    check.append(2)
else:
    check.append(1)
ans = 3 if check[0] == 1 else 6
for i in range(1,len(check)):
    if check[i-1] == 1:
        ans *= 2
    elif check[i] == 2 and check[i-1] == 2:
        ans *= 3
print(ans%MOD)