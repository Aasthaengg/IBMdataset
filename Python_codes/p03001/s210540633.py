W,H,x,y=map(int,input().split())

if W%2==0 and x==W//2 and H%2==0 and y==H//2:
    print("{:.09f}".format(W*H/2),1)
else:
    print("{:.09f}".format(W*H/2),0)
