N = int(input())
D, X = map(int, input().split())

count = 0
for i in range(N):
  A = int(input())
  count += int((D - 1) / A) + 1
  
print(count + X)  








