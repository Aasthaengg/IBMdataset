#123456789
#255456376
n, m = map(int, input().split())
a = list(map(int , input().split()))
a.sort()
t = [2,5,5,4,5,6,3,7,6]
cost = []
for i in range(m):
    cost.append(t[a[i]-1])
#print(a)
#print(cost)
min_c = min(cost)
digit = n // min_c # 最大桁数
s = n % min_c # 最大桁まで作った余りの本数

max_ai = 0
import itertools
for i in itertools.product(list(range(m+1)), repeat=min(digit, 5)):
    #print(i)
    t = list(i)
    ci = sum(list(map(lambda j: cost[j-1] if j != 0 else 0, t)))
    ai = ''.join(map(lambda j: str(a[j-1]) if j != 0 else '', t))
    if digit <= 5:
        if ci == n:
            max_ai = max(max_ai, int(ai))
    else:
        if ci == (n - min_c * (digit - 5)):
            max_ai = max(max_ai, int(ai))
    #print(ci, max_ai)
min_chr = ''
for i in reversed(range(m)):
    if min_c == cost[i]:
        min_chr = a[i]
        break

if digit <= 5:
    print(max_ai)
else:
    ans = list(str(max_ai)) + ([str(min_chr)] * (digit - 5))
    ans.sort(reverse=True)
    print(''.join(ans))


"""
chg = []
while s > 0:
    #print(s, chg)
    for i in reversed(range(m)):
        if min_c + s == cost[i]:
            chg.append(a[i])
            s = 0
            break
    for i in reversed(range(m)):
        if min_c < cost[i] and cost[i] < min_c + s:
            chg.append(a[i])
            s = min_c + s - cost[i]
            break

#print(chg)
min_chr = ''
for i in reversed(range(m)):
    if min_c == cost[i]:
        min_chr = a[i]
        break

ans = chg + ([min_chr] * (d - len(chg)))
ans.sort(reverse=True)
print(''.join(map(str, ans)))
"""