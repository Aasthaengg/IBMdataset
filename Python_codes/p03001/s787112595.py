W,H,x,y = map(int,input().split())

max = W*H/2
many = 1 if x==W/2 and y==H/2 else 0
print(max,many)