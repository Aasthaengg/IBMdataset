a = int(input())
b = int(input())

n = [1,2,3]
n[a-1] = 0
n[b-1] = 0

for i in range(len(n)):
  if n[i] != 0:
    print(n[i])