n = int(input())
l = list(map(int,input().split()))
c= 0

for i in range(n):
  for j in range(n):
    for k in range(n):
      if l[i] + l[j] > l[k] and l[j]+l[k]>l[i] and l[k]+l[i]>l[j]  and i<j and j<k and l[i] != l[j] != l[k] != l[i]:
        c += 1

print(c)
