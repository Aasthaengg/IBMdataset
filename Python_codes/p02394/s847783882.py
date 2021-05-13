W,H,x,y,r=map(int,raw_input().split())
if not(-100<=x and y<=100 and 0<W<=100 and 0<H<=100 and 0<r<=100):
    print("Constraits Errand")
    exit()
#elif x<=0 or y<=0 or  y-r<=H<=y+r or x-r<=W<=x+r or  y-r<=0<=y+r or x-r<=0<=x+r:
elif r<=x<=W-r and r<=y<= H-r:
    print("Yes")
else:
    print("No")