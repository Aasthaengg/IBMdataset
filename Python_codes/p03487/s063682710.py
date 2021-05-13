n = int(input())
a = list(map(int, input().split()))
b = []
c = {}
ans = 0
for i in range(n):
  if a[i] in c:
    c[a[i]] += 1
  else:
    c[a[i]] = 1
    b.append(a[i])
  
for i in range(len(b)):
  temp=c[b[i]]
  temp2=b[i] 
  if temp > temp2:
    ans += temp-temp2
  elif temp < temp2:
    ans += temp
  
  
print(ans)
