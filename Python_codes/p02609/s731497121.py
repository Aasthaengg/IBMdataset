n = int(input())
sn = input()
sr = ''.join(list(reversed(sn)))
sint = int(sn, 2)
spop = sn.count('1')

def f(x):
    count = 0
    while x != 0:
        count += 1
        pop = bin(x).count('1')
        x %= pop
    return count



m1 = sint % (spop + 1)
m2 = 0 if spop <= 1 else sint % (spop - 1)

a = [0] * n
for i in range(n):
    if sr[i] == '0':
        d = pow(2, i, spop + 1)
        m = (m1 + d) % (spop + 1)
        a[i] = f(m) + 1
    elif spop != 1:
        d = pow(2, i, spop - 1)
        m = (m2 - d + spop - 1) % (spop - 1)
        a[i] = f(m) + 1
    else:
        a[i] = 0

for ans in reversed(a):
    print(ans)
