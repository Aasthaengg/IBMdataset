n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

result = -1
for i in range(n):
  a_sum = sum(a[0:i+1])
  result = max(result, a_sum + sum(b[i:]))
  
print(result)