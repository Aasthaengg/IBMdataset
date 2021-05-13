a,b = map(int,input().split())
T = 0

for n in range(1,b-a+1):
  T+=n

print(T-b)