n,x = map(int,input().split())
l = list(map(int,input().split()))
count = []
for i in range(n+1):
  if i == 0:
    d =0
  else:
    d += l[i-1]
  count.append(d)
      
print(len([i for i in count if i <= x]))