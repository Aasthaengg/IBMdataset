N,H,W = map(int,input().split())
count = 0;
for i in range(N):
  h1,w1 = map(int,input().split());
  if h1 >= H and w1 >= W: 
    count = count + 1;
print(count)