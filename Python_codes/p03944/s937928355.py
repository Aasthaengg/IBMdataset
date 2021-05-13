W,H,N = map(int,input().split())
w = W*[1]
h = H*[1]

for n in range(N):
  x,y,a = map(int,input().split())
  if a == 1:
    w[:x] = x*[0]
  elif a == 2:
    w[x:] = (W-x)*[0]
  elif a == 3:
    h[:y] = y*[0]
  else:
    h[y:] = (H-y)*[0]

print(w.count(1)*h.count(1))
