a = list(map(int,input().split()))
min = 100000

for i in range(3):
  if min > (a[i%3] + a[(i+1)%3]):
    min = a[i%3] + a[(i+1)%3]
    
print(min)