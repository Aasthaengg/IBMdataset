arr = input().split()

n = int(arr[0])
l = int(arr[1])
s = 0
arr2 = []
for i in range(0,n):
  s += l + i
  arr2.append(l + i)
  
minimum = l + n - 1

for i in range(0, n):
  minimum = min(minimum, abs(arr2[i]))
  
print(s-minimum)
                
 
