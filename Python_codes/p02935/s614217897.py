n = int(input())
v = sorted(list(map(int,input().split())))

for i in range(n-1):
  v[0] =(v[0] + v[1])/2
  del v[1]

print(v[0])