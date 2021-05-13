x=0
y=0
n=int(input())
for i in range(n):
    s,t=map(str,input().split())
    if s==t : 
        x+=1
        y+=1 
    elif s>t : x+=3
    else : y+=3
print(x,y)
