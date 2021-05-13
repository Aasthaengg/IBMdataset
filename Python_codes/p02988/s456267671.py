n = input()
p = [int(z) for z in input().split()]
c=0
for i in range(1,len(p)-1):
      if (p[i-1]<=p[i]<=p[i+1] or p[i+1]<=p[i]<=p[i-1]):
            c+=1
print(c)
