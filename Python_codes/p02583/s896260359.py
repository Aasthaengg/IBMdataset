n = int(input())
arr = list(map(int, input().split()))

c = 0
h = set([])

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      t = [arr[i], arr[j],arr[k]]
      t.sort()
      if t[0] + t[1] > t[2]:
        if t[0]!=t[1]!=t[2]:#if (i,j,k) not in h:
          h.add((i,j,k))
          c+=1
        
print(c)