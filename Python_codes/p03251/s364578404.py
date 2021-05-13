n,m,x,y = map(int,input().split())
l = list(map(int,input().split()))
r = list(map(int,input().split()))

for i in range(-100,101):
  if x<i and i<=y and max(l)<i and min(r) >= i:
    print("No War")
    exit()
print("War")