W,a,b=map(int,input().split())
if max(a,b)>min(a,b)+W:
    print(max(a,b)-(min(a,b)+W))
else:
    print(0)