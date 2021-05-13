n=int(input())
a=[int(input())for i in range(n)]
x,y=-1,-1
for i in a:
 if i-x>1:print(-1);exit()
 elif i==x+1:y+=1
 else:y+=i
 x=i
print(y)