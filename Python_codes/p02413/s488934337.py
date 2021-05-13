h, w = [int(i) for i in input().split()]
date = [[int(q) for q in input().split()] for e in range(h)]
date2=[]
date3=[]
for r in range(0, h):
    for t in range(0, w):
        print(date[r][t], end=' ')
    print(sum(date[r]))

for k in range(0,w):
   for j in range(0,h):
      date2.append(date[j][k])

for n in range(0,w*h,h):
   print(sum(date2[n:(n+h)]),end=' ')

for m in range(h):
   date3.append(sum(date[m]))
print(sum(date3))