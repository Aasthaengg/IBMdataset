n=int(input())
num = 0
for i in range(n):
  a,b=map(int, input().split())
  num = num + b - a + 1
print(num)
