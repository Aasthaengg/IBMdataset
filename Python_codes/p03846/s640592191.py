import io

data = int(input())
array = list(map(int,input().split()))
array.sort()
modulus = 10**9 + 7
result = (2 ** (data // 2)) % modulus
array2 = []
for i in range(data):
  array2 += [abs(data+1-2*(i+1))]
array2.sort()
if array == array2 :
  print(result)
else:
  print(0)