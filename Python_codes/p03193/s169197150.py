N, H, W = map(int, raw_input().split())
count = 0
for i in range(N):
   A, B = map(int, raw_input().split())
   if H <= A and W <= B:
      count += 1
print(count)