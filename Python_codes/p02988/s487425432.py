n, c = int(input()), 0
l = list(map(int, input().split()))
for i in range(1, n-1):
  if sorted([l[i], l[i+1], l[i-1]])[1]==l[i]: c+=1
print(c)