N = int(input())
l = []
b = int(380000)
t = 0

for i in range (N):
  l.append(list(map(str, input().split())))
  
for j in range (N):
  
  if l[j][1] == "BTC":
    t += float(l[j][0])*b
    
  else:
    t += float(l[j][0])
    
print(t)