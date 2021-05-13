s = input()
x,y = map(int,input().split(" "))
l = [len(c) for c in s.split("T")]
X = l[::2]
Y = l[1::2]
 
ansX = set([X[0]])
for i in range(1,len(X)):
    ansX = set([c+X[i] for c in ansX]+[c-X[i] for c in ansX])
 
ansY = set([0])
for i in range(0,len(Y)):
    ansY = set([c+Y[i] for c in ansY]+[c-Y[i] for c in ansY])
    
if x in ansX and y in ansY:
    print("Yes")
else:
    print("No")
