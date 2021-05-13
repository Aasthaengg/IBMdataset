N = int(input())
S = [0] * 100
c74, c24, c14, c4, c2 = 0, 0, 0, 0, 0
for i in range(2, N + 1):
    a = i
    for j in range(2, i + 1):
        while a % j == 0:
            a //= j 
            S[j] += 1
            if S[j] == 74:
                c74 += 1
            if S[j] == 24:
                c24 += 1
            if S[j] == 14:
                c14 += 1
            if S[j] == 4:
                c4 += 1
            if S[j] == 2:
                c2 += 1
        if a == 1:
            break
ans = c74 + c24 * (c2 - 1) + c14 * (c4 - 1) + c4 * (c4 - 1) * (c2 - 2)  // 2
print(ans)