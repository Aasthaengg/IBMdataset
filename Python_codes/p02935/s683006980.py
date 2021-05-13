N = int(input())
v = list(map(int,input().split()))
v.sort()
result = v[0]

for i in range(N-1):
  result = (result + v[i+1]) / 2
  
print(result)