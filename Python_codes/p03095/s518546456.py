n = int(input())
s = list(input())
mod = 10 ** 9 + 7
alpha = "abcdefghijklmnopqrstuvwxyz"
cnt = []
for a in alpha:
    tmp = s.count(a)
    cnt.append(tmp + 1)
ans = 1
for num in cnt:
    ans *= num
    ans %= mod
print(ans - 1)