n = int(input())
X = [int(i) for i in input().split()]
Y = [int(j) for j in input().split()]
for p in [1,2,3]:
    D = (sum([abs(x-y)**p for (x,y) in zip(X,Y)]))**(1/p)
    print("{:.6f}".format(D))
D = max([abs(x-y) for (x,y) in zip(X,Y)])
print("{:.6f}".format(D))
