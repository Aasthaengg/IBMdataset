A,B,C=map(int,input().split())
X,Y,Z=sorted([A,B,C])

K=0
while Y<Z:
    X+=1
    Y+=1
    K+=1

while X<Y:
    X+=2
    K+=1

if X!=Y:
    K+=1
print(K)
