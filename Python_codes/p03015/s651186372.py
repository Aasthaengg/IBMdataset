L = [int(i) for i in input()]
l = len(L)


def mod_pow(a, p, mod):
    if p == 0:
        return 1
    elif p % 2 == 1:
        return a * mod_pow(a, p - 1, mod)
    else:
        return (mod_pow(a, p // 2, mod) % mod) ** 2 % mod


# L以下の整数は「上からi桁目まで同じで、それ以降違う」で考える。　あるL以下の整数=A+B
# L[i]=0のときAとBの桁は(0,0), L[i]=1のときAとBの桁は(0,1)(1,0)のどちらか
mod = 10 ** 9 + 7
answer = 0
prev = 1

for i, j in enumerate(L, 1):
    if j == 0:
        continue
    answer += prev * mod_pow(3, l - i, mod)
    answer %= mod
    prev *= 2
    prev %= mod

answer += prev
answer %= mod
print(answer)
