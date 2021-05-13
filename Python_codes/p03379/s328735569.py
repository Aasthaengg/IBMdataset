n = int(input())
X = list(map(int,input().split()))
Y = sorted(X)
left = Y[n//2-1]
right = Y[n//2]

for i in X:
    if i <= left:
        print(right)
        
    else:
        print(left)