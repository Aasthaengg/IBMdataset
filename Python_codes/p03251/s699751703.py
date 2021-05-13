n,m,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
s = 1
for i in range(-100,101):
    if X < i <= Y and max(x) < i <= min(y):
        s = 0
print(["No War","War"][s])
