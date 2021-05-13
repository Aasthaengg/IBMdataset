s = input()
k = int(input())

s_sorted = sorted(s)
array = set()

n = len(s)
for i in range(n):
  for j in range(n):
    if s_sorted[i] == s[j]:
      for l in range(k):
        if l+j >= n:
          break
        
        array.add(s[j:l+j+1])
      
  if len(array) >= k:
    break
    
array = sorted(array)
print(array[k-1])