n=int(input())
a=[0]*n
a=map(int,input().split())
    
z=0
result=0
min=1000000002

for i in a:
    if i<0:
        z+=1
    result+=abs(i)
    if abs(i)<min:
        min=abs(i)

if z%2==1:
    result-=min*2

print(result)