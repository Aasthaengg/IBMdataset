n,m,x,y=map(int, input().split())
x_l = list(map(int, input().split()))
y_l = list(map(int, input().split()))
if max(x_l)<y and max(x_l) < min(y_l) and x < min(y_l):
  print("No War")
else:
  print("War")
