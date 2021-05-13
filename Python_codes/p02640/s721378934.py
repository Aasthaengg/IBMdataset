x,y=map(int,input().split())
z=0
for i in range(x+1):
    if 2*i+4*(x-i)==y:
        z=1
print("Yes" if z==1 else "No")