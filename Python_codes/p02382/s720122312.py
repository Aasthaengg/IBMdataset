import math
N = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))
p1 = 0
i = 0
while i < N :
    p1 = p1 + abs(X[i]-Y[i])
    i = i + 1
print(p1)

p2 = 0
i = 0
while i < N :
    p2 = p2 + (X[i]-Y[i])**2
    i = i + 1
print (math.sqrt(p2))

p3 = 0
i = 0
while i < N :
    p3 = p3 + abs((X[i]-Y[i])**3)
    i = i + 1
print(math.pow(p3, (1/3)))

p4 = abs(X[0]-Y[0])
i = 0
while i < N-1 :
    if p4 < abs(X[i+1]-Y[i+1]) :
        p4 = abs(X[i+1]-Y[i+1])
    i = i + 1
print(p4)
