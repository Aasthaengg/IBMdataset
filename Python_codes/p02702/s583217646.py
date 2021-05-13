import sys

S = sys.stdin.readline().strip()
ls = len(S)

mod = 2019
S = S[::-1]

acum = [0] * (ls+1)
counter = {0: 1}
for i, s_i in enumerate(S):
    acum[i+1] = (acum[i] + int(s_i) * pow(10, i, mod)) % mod
    if acum[i+1] not in counter:
        counter[acum[i+1]] = 0
    counter[acum[i+1]] += 1
# print(counter)

# mod が同じものになっている桁の組み合わせなら2019の倍数
ans = 0
for value, count in counter.items():
    ans += count * (count - 1) // 2

print(ans)