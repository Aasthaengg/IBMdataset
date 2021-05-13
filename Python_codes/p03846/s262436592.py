from collections import Counter
n = int(input())
a = list(map(int,input().split()))
comb = 0
c = Counter(a)
if n%2==0:
    i = 1 
else:
    if c[0]!=1:
        print(0)
        exit()
    c.pop(0)
    i = 2

for k in sorted(c):
    if i==k and c[k]==2:
        i+=2
        comb += 1
    else:
        print(0)
        exit()

print(2**comb%(10**9+7))