a,b = map(int,input().split())

d = b - a
x = [1]
for i in range(1,1000):
  x.append(i+1+x[i-1])
  if x[i] - x[i-1] == d:
    break
    
print(x[-1] - b)