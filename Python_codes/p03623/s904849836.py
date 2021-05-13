x,a,b=map(int,input().split())
if (max(x,a)-min(x,a))>(max(x,b)-min(x,b)):
    print("B")
else:
    print("A")
