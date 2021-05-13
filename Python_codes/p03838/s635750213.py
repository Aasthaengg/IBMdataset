x,y = map(int, input().split())
A = []
if 0<=x<=y: A.append(y-x)
if 0<=y<=x: A.append(x-y+2)
if y<=0<=x: A.append(abs(x+y)+1)
if x<=0<=y: A.append(abs(x+y)+1)
if x<=y<=0: A.append(y-x)
if y<=x<=0: A.append(x-y+2)
print(min(A))