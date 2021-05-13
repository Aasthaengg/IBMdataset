a = [1]*45
for i in range(2,len(a)):
  a[i] = a[i-1] + a[i-2]
  
print(a[int(input())])