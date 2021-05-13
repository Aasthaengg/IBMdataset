import sys
a,b,c = map(int,input().split(" "))
li = [[a,b,c]]
count=0

for i in range(10**2):
  if (a % 2)==1 or (b % 2)==1 or (c % 2)==1:
    break
  else:
    a2 = a/2
    b2 = b/2
    c2 = c/2
    a = b2+c2
    b = c2+a2
    c = a2+b2  
    count += 1
  if [a,b,c] in li:
    print(-1)
    sys.exit()
  else:
    li.append([a,b,c])
    
print(count)
