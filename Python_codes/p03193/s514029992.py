N,H,W=map(int, raw_input().split(' '))
cnt=0
for i in range(N):
  a,b=map(int, raw_input().split(' '))
  if a>=H and b>=W:
    cnt += 1
print cnt