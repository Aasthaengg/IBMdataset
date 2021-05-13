#ABC079 C:Train Ticket
import itertools

s = list(input())
num = []
calc = [1, -1]
for i in range(len(s)):
    a = int(s[i])
    num.append(a)

calc_comb = [_ for _ in itertools.product(calc, repeat=3)]

x = 0
while True:
    ans = num[0]
    for i in range(len(num)-1):
        ans += num[i+1] * calc_comb[x][i]

    if ans == 7:
        r = calc_comb[x]
        break
    else:
        x += 1

r_replace = ['+' if i==1 else '-' for i in r]
out = [None] * (len(s)+len(r_replace))
out[::2] = s
out[1::2] = r_replace
out = ''.join(out)
print(out, '=7', sep='')
