n = int(input())
v = list(map(int,input().split()))
v.sort()

for i in range(0,n-1):
  sum = (v[i] + v[i+1])/ 2
  v[i+1] = sum 

print(v[n-1])