import sys
N,L = map(int,input().split())
apple = []
diff =1000000
num = 0
for i in range(N):
  value = i + L
  apple.append(value)
  if diff > abs(value):
    diff = abs(value)
    num = i
del apple[num]
print(sum(apple))