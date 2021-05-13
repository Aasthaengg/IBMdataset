n = int(input())
a,b = map(int,input().split())
P = list(map(int,input().split()))

Q = [0]*3
for i in range(n):
  if P[i] <= a:
    Q[0] += 1
  elif P[i] <= b:
    Q[1] += 1
  else:
    Q[2] += 1
    
print(min(Q))    