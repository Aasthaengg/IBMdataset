from collections import Counter
N = 1000000007
n = int(input())
s = input()
c = Counter(s)
k = c.keys()
ans = 1
for i in k:
    ans *= (c[i]+1)
    ans %= N
if ans!=0:
    ans -= 1
print(ans)
