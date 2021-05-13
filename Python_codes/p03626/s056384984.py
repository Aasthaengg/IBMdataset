N = int(input())
A = input()
B = input()

ptn = []
i = 0
while i < N:
    if A[i] == B[i]:
        ptn.append(1)
        i += 1
    else:
        ptn.append(2)
        i += 2

MOD = 10**9+7
ans = 3 * ptn[0]
for a,b in zip(ptn,ptn[1:]):
    if a == 1 and b == 1:
        ans *= 2
    elif a == 1 and b == 2:
        ans *= 2
    elif a == 2 and b == 2:
        ans *= 3
    ans %= MOD
print(ans)
