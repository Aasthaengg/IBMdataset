N=int(input())
h=list(map(int,input().split()))
while len(h)>=2:
    if h[0]-h[1]>=2:
        print("No")
        break
    else:
        if h[0]<=h[1]:
            h.pop(0)
        else:
            h.pop(1)
if len(h)<=1:
    print("Yes")
else:
    pass