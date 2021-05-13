N = int(input())
X = input()

a = int(X, 2)
b = X.count("1")

if b > 1:
    a1 = a % (b-1)
else:
    a1 = 0
a0 = a % (b+1)

for i in range(N):
    if X[i] == "1":
        if b == 1:
            print(0)
            continue
        t = (a1 - pow(2, N-1-i, b-1)) % (b-1)
    else:
        t = (a0 + pow(2, N-1-i, b+1)) % (b+1)
    
    ans = 1
    while t > 0:
        t %= bin(t).count("1")
        ans += 1
    print(ans)
