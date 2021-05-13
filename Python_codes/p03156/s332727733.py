n = int(input())
a,b = map(int,input().split())
l = list(map(int,input().split()))

x,y,z=0,0,0
for i in l:
    if i<=a: x+=1
    elif i >=b+1: z+=1
    else: y+=1

print(min(x,y,z))