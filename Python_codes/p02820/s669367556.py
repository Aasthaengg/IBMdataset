def inp(r, s, p, jan):
  if jan == 's':
    return r
  elif jan == 'p':
    return s
  else:
    return p

n, k = map(int, input().split(" "))
r,s,p = map(int, input().split(" "))
t = list(input())
total = 0
for i in range(n):
  if i < k:
    #print(2)
    total += inp(r,s,p,t[i])
  else:
    if t[i] != t[i-k]:
      #print("OK")
      total += inp(r,s,p,t[i])
    else:
      #print("NG")
      t[i] = 'x'
print(total)