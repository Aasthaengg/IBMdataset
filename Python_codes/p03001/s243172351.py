W,H,x,y = list(map(int,input().split()))

ans_1 = W*H/2
ans_2 = 0
if x == W/2 and y == H/2:
  ans_2 = 1
  
print(ans_1,ans_2)