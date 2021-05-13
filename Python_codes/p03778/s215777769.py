W,a,b=map(int,input().split())
if abs(a-b)>=W:
    print(abs(W-abs(a-b)))
else:
    print(0)
