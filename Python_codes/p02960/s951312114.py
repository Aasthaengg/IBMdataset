s = list(input())[::-1]
n = len(s)
mod = 10**9 + 7

t = [[0 for j in range(13)] for i in range(n)]
for i,x in enumerate(s):
    A = pow(10, i ,13)
    if i == 0:
        if x == "?":
            for j in range(0,10):
                t[i][j] += 1
        else:
            t[i][int(x)] += 1
    else:
        if x == "?":
            for k in range(13):
                for j in range(10):
                    b = (k + j*A)%13
                    t[i][b] += t[i-1][k]
                    t[i][b] %= mod
        else:
            for k in range(0,13):
                b = (k + int(x)*A)%13
                t[i][b] += t[i-1][k]
                t[i][b] %= mod
print(t[-1][5]%mod)
