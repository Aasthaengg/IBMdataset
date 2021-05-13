N = int(input())
ABs = []
As = []
Bs = []

tk = 0
ao = 0

for i in range(N):
  a,b = map(int, input().split())
  As.append(a)
  Bs.append(b)
  ABs.append((a+b, i))
  
ABs.sort(key=lambda x:x[0], reverse=True)

for i in range(N):
  if i%2 == 0:
    tk += As[ABs[i][1]]
  else:
    ao += Bs[ABs[i][1]]
    
print(tk-ao)