import collections

TEISUU = 1000000007

S = input()
N = input()
c = collections.Counter(N)
lis = list(c.values())
ans = 1
for count in lis:
    ans *= int(count + 1)
    
ans -= 1
print(ans % TEISUU)

