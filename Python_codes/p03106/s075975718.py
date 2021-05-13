abk = [int(i) for i in input().split()]
a = abk[0]
b = abk[1]
k = abk[2]

anss = []
for i in range(1,min(a,b)+1):
  if a%i==0 and b%i==0:
    anss.append(i)
    
anss.sort(reverse=True)
print(anss[k-1])
