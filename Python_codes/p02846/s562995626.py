t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
if a1*t1+a2*t2==b1*t1+b2*t2:
    print("infinity")
    quit()
x = (a1-b1)*t1
y = (a2-b2)*t2
if x < 0:
    x,y = -x,-y
d = x+y
if d > 0:
    print(0)
    quit()
if x%(-d) == 0:
    print(2*(x//(-d)))
else:
    print(2*(x//(-d))+1)

