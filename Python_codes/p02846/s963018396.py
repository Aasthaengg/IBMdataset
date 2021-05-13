t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())

x1 = (a1-b1) * t1
x2 = (a2-b2) * t2 + x1
      
if x2 ==0:
    print("infinity")
elif x1*x2>0:
    print(0)
else:
    print(abs(x1) // abs(x2) * 2 + (abs(x1)%abs(x2) > 0))