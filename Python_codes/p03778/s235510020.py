W,a,b=map(int,input().split())
print(0 if(a<=b and b<=a+W)or(a<=b+W and b+W<=a+W)else abs(a-b)-W)