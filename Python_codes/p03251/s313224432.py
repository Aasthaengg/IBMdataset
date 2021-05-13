
n,m,x,y = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
X.append(x)
Y.append(y)
X.sort()
Y.sort()

for i in range(-100,100):
    if X[-1] < i <= Y[0]:
        print("No War")
        exit()

print("War")

