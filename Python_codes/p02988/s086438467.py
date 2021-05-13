a = int(input())
b = list(map(int,input().split()))
c = 0
for i in range(1,a-1):
  if b[i-1]<b[i] and b[i]<b[i+1]:
    c += 1
  elif b[i-1]>b[i] and b[i]>b[i+1]:
    c += 1
print(c)