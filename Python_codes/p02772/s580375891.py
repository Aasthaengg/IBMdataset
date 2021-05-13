N = int(input())
A = list(map(int,input().split(" ")))
B = ["APPROVED","DENIED"]
t = 0

for i in A:
  if i%2 == 0:
    if i%3 != 0 and i%5 != 0:
      t = 1
      break
print(B[t])