import fractions

def lcm(x,y):
    return x*y//fractions.gcd(x,y)

N, M = map(int, input().split())
S = input()
T = input()

L = lcm(N,M)
ST_idx = set([i*(L//N) for i in range(N)]) & set([i*(L//M) for i in range(M)])

for x in ST_idx:
    if S[(N*x)//L] != T[(M*x)//L]:
        print(-1)
        break
else:
    print(L)