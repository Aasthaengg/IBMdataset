n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
anslist = []

for i in range(1,n-1):
  if a[i] < 0:
    anslist.append([a[-1], a[i]])
    a[-1] -= a[i]
  else:
    anslist.append([a[0], a[i]])
    a[0] -= a[i]
anslist.append([a[-1], a[0]])
ans = a[-1]-a[0]
print(ans)
for i in range(len(anslist)):
  print(anslist[i][0], anslist[i][1])
    
  
      
