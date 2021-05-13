y = [int(z) for z in input().split()]
l = [int(z) for z in input().split()]
d = [0]*(y[0]+1)
c = 1
for i in range(1,y[0]+1):
      d[i] = d[i-1]+l[i-1]
      if (d[i]<=y[1]):
            c+=1
print(c)
