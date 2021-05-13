n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x = sum(a)
for i in range(len(b)):
  if a[i]+a[i+1]<b[i]:
    a[i] = 0
    a[i+1] = 0
  elif a[i]<b[i]:
    a[i+1] = a[i]+a[i+1]-b[i]
    a[i] = 0
  else:
    a[i]-=b[i]
    
print(x-sum(a))