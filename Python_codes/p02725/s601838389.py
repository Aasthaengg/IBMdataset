k,n = map(int,input().split(" "))
a = list(map(int,input().split(" ")))
d_max = a[0]+(k-a[n-1])
d_max_i = n-1 
for i in range(1,n):
  if a[i] - a[i-1] > d_max:
    d_max = a[i] - a[i-1]
print(k-d_max)