z,y,x = sorted(list(map(int,input().split())))
print((3*x-(x+y+z))//2 if (3*x-(x+y+z))%2==0 else (3*x-(x+y+z))//2+2)