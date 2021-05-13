k,x = map(int,input().split())

c = []

for i in range(-k+1,k):
  c.append(x-i)
  
c.sort()
t = [str(i) for i in c]
print(' '.join(t))