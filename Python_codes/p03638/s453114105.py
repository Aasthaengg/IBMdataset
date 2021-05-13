H, W, N, *a = map(int, open(0).read().split())
l = []
for i in range(N):
  l += [i+1]*a[i]
for i in range(H):
  print(*l[i*W:(i+1)*W][::1-i%2*2])