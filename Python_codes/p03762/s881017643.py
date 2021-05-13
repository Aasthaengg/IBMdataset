n, m = map(int, input().split())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
mod = 7 + 10**9

xtotal, ytotal = 0, 0
for i in range(n-1):
    xarea = x[i+1] - x[i]
    xright, xleft =  n - i - 1, i + 1
    xtotal += (xarea * xright * xleft) %mod
    xtotal %= mod
for j in range(m-1):
    yarea = y[j+1] - y[j]
    yup = m - j -1
    ydown = j + 1
    ytotal += (yarea * yup * ydown) % mod
    ytotal % mod

print((xtotal * ytotal) % mod)