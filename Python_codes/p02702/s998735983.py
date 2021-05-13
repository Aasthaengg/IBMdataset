S = input()
mod = 2019
count = [0] * 2019
count[0] = 1
tmp = 0
d = 1

for s in S[::-1]:
    tmp += int(s) * d
    count[tmp % mod] += 1
    d *= 10
    d %= mod

ans = 0

for c in count:
    ans += c * (c - 1) // 2
        
print(ans)