a,b=map(int,input().split())
l=[]
for i in range(b-a+1,a+b):
    l.append(str(i))

for j in l:
    print(j,end=" ")