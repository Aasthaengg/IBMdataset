a = list(map(int,input().split()))
x = []
for i in range(2):
  for j in range(2,4):
    x.append(a[i]*a[j])

print(max(x))
