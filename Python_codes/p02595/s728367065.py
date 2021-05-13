N,D = map(int,input().split())
count = 0
for i in range(N):
  X,Y = map(int,input().split())
  if X*X + Y*Y<=D*D:
    count += 1
print(count)
