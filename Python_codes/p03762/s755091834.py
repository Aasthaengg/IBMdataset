
n,m =list(map(int,input().split(" ")))
xs  =list(map(int,input().split(" ")))
ys =list(map(int,input().split(" ")))
MOD = (10**9) + 7
x_diff = [abs(i - j) for i,j in zip(xs[:n-1],xs[1:n]) ]
y_diff = [abs(i - j) for i,j in zip(ys[:m-1],ys[1:m]) ]

cot = 1
x = 0
for i in range(n -1 ):
    x +=cot * (n-i -1) * x_diff[i]
    cot += 1

cot = 1
y = 0
for i in range(m -1):
    y += cot * (m-i -1) * y_diff[i]
    cot += 1



print (x* y % MOD )
