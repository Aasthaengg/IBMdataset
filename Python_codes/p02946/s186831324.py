a,b=map(int,input().split())
x=[]
for i in range(b-a+1,b+a):
  x.append(str(i))
print(' '.join(x))