n = int(input())
a = [0]*n

for i in range(n):
  a[i] = int(input())
  
a.sort()
a.append(-1)
ans = []
cn = 0
c = 1
#print(a)
for i in range(n):
  if a[i] != a[i+1]:
    ans.append(c)
    c = 1
  else:
    c += 1
#print(ans)

for i in range(len(ans)):
  if ans[i]%2 == 1:
    cn += 1
    
print(cn)