a = list(input())
b = 0;
for i in range(2, len(a)):
  x = int(a[i-2]+a[i-1]+a[i])
  if abs(753-b) > abs(753-x):
    b = x 
print(abs(b-753))