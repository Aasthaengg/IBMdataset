a,b,x = map(int,input().split())
fb = b//x+1
if a!= 0 :
    fa = (a-1)//x+1
else :
    fa = 0
print(fb-fa)