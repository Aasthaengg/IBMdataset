n = int (input())
k = int (input())

num = 1
for i in range(n):
  num = num * 2 if num <= k else num + k
  
print (num)