n = int(input())
A = list(map(int, input().split()))

mod = 10**9+7
X = [0]*62
for i in range(n):
    a = A[i]
    b = format(a, 'b')
    b = list(b)
    b.reverse()
    for j in range(len(b)):
        if b[j] == '1':
            X[j] += 1
ans = 0
for i in range(62):
    x = X[i]
    y = n-X[i]
    #print(i, x, y)
    ans += x*y*pow(2, i, mod)
ans %= mod
print(ans)
