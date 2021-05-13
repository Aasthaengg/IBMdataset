N,K,Q = map(int,input().split())
A = [int(input()) for i in range(Q)]
num = K-Q
point = [num]*N

for a in A:
  point[a-1] += 1

for po in point:
  if po > 0:
    print("Yes")
  else:
    print("No")