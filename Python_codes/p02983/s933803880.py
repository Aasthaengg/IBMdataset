l,r=map(int,input().split())
if r-l>672: print(0); exit()
m=[i%2019 for i in range(l,r+1)]
a=2019
for i in m:
  for j in m:
    if i<j: a=min(a,i*j%2019)
print(a)