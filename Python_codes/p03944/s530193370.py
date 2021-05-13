w,h,n = map(int,input().split())
W = ["."] * w
H = ["."] * h

for _ in range(n):
  x,y,a = map(int,input().split())
  
  if a==1:
    tmp = ["#"]*x + W[x:]
    W = tmp
  elif a==2:
    tmp = W[:x] + ["#"]
    W = tmp
  elif a==3:
    tmp = ["#"]*y + H[y:]
    H = tmp
  elif a==4:
    tmp = H[:y] + ["#"]
    H = tmp
    
print(W.count('.')*H.count('.'))
