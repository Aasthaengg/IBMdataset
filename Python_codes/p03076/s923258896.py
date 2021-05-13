A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
X=[A%10,B%10,C%10,D%10,E%10]
minimum=100
for i in range(5):
  if X[i]!=0:
    minimum=min(minimum,X[i])
Y=[A,B,C,D,E]
if minimum==100:
  minimum=0
last=X.index(minimum)
time=0
import math
for i in range(5):
  if i!=last:
    time =time+10*math.ceil(Y[i]/10)
if X==[0,0,0,0,0]:
  print(sum(Y))
else:
  print(time+Y[last])