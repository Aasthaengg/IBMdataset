n = int(input())
x = list(map(int,input().split()))
y = sorted(x)

for i in range(n):
  if x[i] <= y[(n//2) - 1]:
    print(y[(n//2)])
  elif x[i] >= y[(n//2)]:
    print(y[(n//2) - 1])