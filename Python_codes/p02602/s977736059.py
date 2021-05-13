n, k = map(int, input().split())
a = list(map(int, input().split()))
#point = 1
t = 0
"""for i in range(t, n):
  point = point*a[i]"""
  
#print(point)
#t = 0
for j in range(k, n):
  #point0 = point
  #point = point*a[j]/a[t]
  if a[j] > a[t]:
    print("Yes")
  else:
    print("No")
  t+=1

