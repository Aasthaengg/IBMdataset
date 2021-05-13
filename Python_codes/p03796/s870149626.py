n=int(input())
num = 1
div=int(1e9)+7
for i in range(1,n+1):
  num = num*i%div
print(num)