n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))
x,y,z = 0,0,0
for i in p:
    if i <= a:
        x += 1
    elif b+1 <= i:
        z += 1
    else:
        y += 1
print(min(x,y,z))