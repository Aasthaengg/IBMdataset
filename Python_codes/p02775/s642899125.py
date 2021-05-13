#import sys
#inf = sys.maxsize

n = str(input())
#l = len(str(n))

'''
a = []
for i in range(l):
    if m[i] <= 5:
        a.append(0)
    elif m[i] > 5:
        a.append(1)

for i in range(l):
    if i < l-1 and a[i+1] == 1 and m[i] == 5:
        a[i] = 1

p = []
for i in range(l):
    if a[i] == 0:
        if i < l-1 and a[i+1] == 1:
            p.append(m[i]+1)
        else:
            p.append(m[i])
    elif a[i] == 1:
        p.append(0)

pp = ''
for i in range(l):
    pp += str(p[i])
if pp[0] == '0':
    pp = '1' + pp
pp = int(pp)
oo = pp - n
print(pp)
print(oo)
ppp = [int(str(pp)[i]) for i in range(len(str(pp)))]
ooo = [int(str(oo)[i]) for i in range(len(str(oo)))]

print(sum(ppp) + sum(ooo))
'''
dp = [0, 1] #dp[0]: ちょうど dp[1]: 1多い

for i in n:
    i = int(i)
    dp0 = dp[0]
    dp1 = dp[1]
    dp[0] = min(dp0 + i, dp1 + (10 - i))
    dp[1] = min(dp0 + i + 1, dp1 + (10 - i) - 1)
print(dp[0])
