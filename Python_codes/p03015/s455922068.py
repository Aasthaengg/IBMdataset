l = input()
n = len(l)
mod = 10 ** 9 + 7
memo = [1]
memo2 = [1]

for i in range(n):
    memo.append(memo[-1] * 3 % mod)
    memo2.append(memo2[-1] * 2 % mod)

i = 1
j = -1
ans = 0

for c in l:
    if c == '1':
        j += 1
        ans += (memo[n-i] ) * memo2[j]
        ans %= mod
    i+=1
ans += memo2[j+1]
ans %= mod
print(ans)
