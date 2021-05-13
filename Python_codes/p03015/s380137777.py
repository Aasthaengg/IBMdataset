L = [int(i) for i in input()]
l = len(L)

# L以下の整数は「上からi桁目まで同じで、それ以降違う」で考える。　あるL以下の整数=A+B
# L[i]=0のときAとBの桁は(0,0), L[i]=1のときAとBの桁は(0,1)(1,0)のどちらか
mod = 10 ** 9 + 7
answer = 0
mod_pow = [0] * (l + 1)
prev = 1
mod_pow[0] = 1


for i in range(1, l + 1):
    prev *= 3
    prev %= mod
    mod_pow[i] = prev

prev = 1
for i, j in enumerate(L, 1):
    if j == 0:
        continue
    answer += prev * mod_pow[l - i]
    answer %= mod
    prev *= 2
    prev %= mod

answer += prev
answer %= mod
print(answer)
