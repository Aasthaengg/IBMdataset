N = int(input())
S1 = input()
S2 = input()

MOD = 10**9 + 7

pre = [S1[0], S2[0]]
ans = 6 if pre[0] != pre[1] else 3
for i in range(1,N):
    current =[S1[i], S2[i]]
    if pre[0] == pre[1]:
        if current[0] == current[1]:
            ans *= 2
            ans %= MOD
        else:
            ans *= 2
            ans %= MOD
    else:
        if current[0] != current[1] and pre[0] != current[0]:
            ans *= 3
            ans %= MOD
    pre = current[:]
print(ans)