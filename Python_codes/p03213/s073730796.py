from collections import defaultdict


def factorization(n):
    global ND
    temp = n
    flag = True
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            flag = False
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            ND[i] += cnt

    if temp!=1:
        ND[temp] +=1
        flag = False

    if flag:
        ND[n] += 1

    return


N = int(input())
ND = defaultdict(int)
for i in range(2, N+1):
    factorization(i)

L2 = 0
L4 = 0
L14 = 0
L24 = 0
L74 = 0

for key, value in ND.items():
    if value >= 2:
        L2 += 1
    if value >= 4:
        L4 += 1
    if value >= 14:
        L14 += 1
    if value >= 24:
        L24 += 1
    if value >= 74:
        L74 += 1

ans = 0
ans += L4 * (L4-1)//2 * (L2 - 2)
ans += L24 * (L2 - 1)
ans += L14 * (L4 - 1)
ans += L74
print(ans)