a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

from itertools import permutations

def ceil_base10(x):
    q,r = divmod(x, 10)
    return 10*(q + min(r, 1))

ans=10**12
for A,B,C,D,E in permutations([a,b,c,d,e], 5):
    s = sum([ceil_base10(x) for x in [A,B,C,D]]) + E
    ans = min(ans, s)

print(ans)
