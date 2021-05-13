n=int(input())
a=list(map(int,input().split()))
m=n//2
x=[a[i] for i in range(n) if i%2==0] #kisuu
y=[a[i] for i in range(n) if i%2==1] #guusuu
x=sorted(x)
y=sorted(y)
inx=[]
iny=[]
p=1
q=1

for i in range(m-1):
    if x[i]==x[i+1]:
        p+=1
    else:
        inx.append([p,x[i]])
        p=1
inx.append([p,x[-1]])
for i in range(m-1):
    if y[i]==y[i+1]:
        q+=1
    else:
        iny.append([q,y[i]])
        q=1
iny.append([q,y[-1]])
inx=sorted(inx)
iny=sorted(iny)
inx.insert(0,[0,0])
iny.insert(0,[0,0])

if inx[-1][1]!=iny[-1][1]:
    print(2*m-inx[-1][0]-iny[-1][0])
else:
    print(min(2*m-inx[-1][0]-iny[-2][0],2*m-inx[-2][0]-iny[-1][0]))
    
        


