N = int(input())
rabit = input().split(" ")
skip = []
num = 0

for i in range(N):
  n = int(rabit[i])
  if n < i+1:
    continue
  if int(rabit[n-1]) == i+1:
    num += 1

print(num)