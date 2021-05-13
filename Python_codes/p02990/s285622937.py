MOD = int(1e9) + 7
n, k = map(int,input().split())
comb = [[0] * 4002 for i in range(4002)]
comb[0][0] = 1
for i in range(1,4001):
    for j in range(4001):
        comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % (int(1e9)+7)
#print(comb)

def f2(x,y):
    if y < 1 or x < 0:
        return 0
    else:
        return comb[x+y-1][y-1]
def f(x,y):
    if x < y:
        return 0
    elif x == 0 and y == 0:
        return 1
    else:
        return f2(x-y,y)

for i in range(1, k+1):
    blue = f(k,i) % MOD
    red = 0
    red += f(n-k,i-1)
    red += f(n-k,i) * 2
    red += f(n-k,i+1)
    red %= MOD
    print((blue * red) % MOD)
