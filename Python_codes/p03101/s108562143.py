H,W=map(int, input().split()) 
h,w=map(int, input().split())
ans = (H-h)*(W-w)
if ans >=0:
    print(ans)
else:
    print(0)