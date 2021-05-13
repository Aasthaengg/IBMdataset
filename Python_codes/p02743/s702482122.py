a,b,c = map(int,input().split())
if c-a-b>0:
    if 4*(a*b)<(c-a-b)**2:
        print("Yes")
    else:
        print("No")
else:
    if a+b+2*(a*b)**0.5<c:
        print("Yes")
    else:
        print("No")