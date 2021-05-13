W, H, x, y = map(int, input().split())

ans = W * H / 2
cent = 0
if (x==W/2) and (y==H/2):
  cent = 1
  
print(ans, cent)