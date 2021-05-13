import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
MOD = 10**9+7
xacc, yacc = [0], [0]

for i in range(n-1):
    xacc.append((xacc[-1]+x[i+1]-x[i])%MOD)

for i in range(m-1):
    yacc.append((yacc[-1]+y[i+1]-y[i])%MOD)

X, t = 0, 0

for i in range(1, n):
    X += i*xacc[i]-t
    X %= MOD
    t += xacc[i]

Y, t = 0, 0

for i in range(1, m):
    Y += i*yacc[i]-t
    Y %= MOD
    t += yacc[i]

print(X*Y%MOD)