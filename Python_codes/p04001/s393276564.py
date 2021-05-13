S = list(map(int, list(input())))
L = len(S)
ans = 0
for bit in range(2**(L-1)):
    temp = 0

    for i in range(L-1):
        temp =temp*10 + S[i]
        if bit & (1<<i):
            ans += temp
            temp = 0
    temp  = temp*10 + S[-1]
    ans += temp


print(ans)

