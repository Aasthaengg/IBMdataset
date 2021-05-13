a,b,c,d,e,f = map(int,input().split())
X = []
Y = []
res = 0
for i in range(f+1):
    for j in range(f+1):
        x = 100*a*i+100*b*j
        y = c*i+d*j
        if x > f and y > f:break
        X.append(x)
        Y.append(y)
def ok(x,y):
    return (x//100)*e >= y and x+y <=f
cnt = 0
X.sort()
Y.sort()
ansx = 0
ansy = 0
for x in X:
    for y in Y:
        if x+y > f:break
        
        if ok(x,y):
          
            if x+y == 0:continue
            if res <= 100*y/(x+y):
                res = 100*y/(x+y)
                ansx = x
                ansy = y
        cnt +=1
print(ansx+ansy,ansy)
