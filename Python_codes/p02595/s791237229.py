N, D = map(int, input().split())
count = 0

for _ in range(N):
   X, Y = map(int, input().split())
   if (X*X + Y*Y)**0.5 <= D:
       count += 1
print(count)