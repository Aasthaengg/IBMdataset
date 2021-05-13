MOD = 10**9 + 7
N = int(input())
S1 = input()
S2 = input()
check = []
index = 0
while index < N:
    if S1[index] == S2[index]:
        check.append(1)
        index += 1
    else:
        check.append(2)
        index += 2
ans = 3 if check[0] == 1 else 6
for i in range(1,len(check)):
    if check[i-1] == 1:
        ans *= 2
    elif check[i] == 2:
        ans *= 3
    ans %= MOD
print(ans)