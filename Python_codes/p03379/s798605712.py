N = int(input())
X = list(map(int,input().split()))
Y = sorted(X)

a = Y[(N-1)//2]
b = Y[(N+1)//2]

for i in X:
    if i > a:
        print(a)
    else:
        print(b)