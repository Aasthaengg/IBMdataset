a,b =map(int,input().split())
for i in range(1,1000):
  c = int(i*(i+1)/2)
  d = int((i+1)*(i+2)/2)
  c = c-a
  d = d-b
  if c ==d:
    print(c)
    break
 