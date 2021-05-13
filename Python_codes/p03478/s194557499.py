n,a,b = list(map(int, input().split()))
array = []
array2 = []

def degitSum(n):
  s = str(n)
  array = list(map(int,s))
  return sum(array)

for i in range(1,n+1):
  if degitSum(i) >= a and degitSum(i) <= b:
    array2.append(i)
    
print(sum(array2))