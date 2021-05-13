W,H,x,y,r=map(int,raw_input().split())
print'Yes'if(r<=x and(W-r)>=x)and(r<=y and(H-r)>=y)else'No'