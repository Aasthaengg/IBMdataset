n=int(input())
A=[int(x) for x in input().split()]
B=sorted(A)
Alice=[]
Bob=[]
while len(B)!=0 and len(B)!=1:
  Alice.append(B[-1])
  B.pop()
  Bob.append(B[-1])
  B.pop()
if len(B)==1:
  Alice.append(B[0])
  B.pop()
print(sum(Alice)-sum(Bob))
