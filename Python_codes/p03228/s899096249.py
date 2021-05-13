a,b,k = map(int,input().split())

for i in range(k):
    a -= a%2
    b += a//2
    a -= a//2
    a,b = b,a
if(k%2 == 1):
  a,b = b,a
print(a,b)
