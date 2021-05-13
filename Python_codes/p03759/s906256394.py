x = list(map(int, input().split()))
X = sorted(x,reverse=True)
if X[0]-X[1] ==X[1]-X[2]:
    print("YES")
else:
    print('NO')
