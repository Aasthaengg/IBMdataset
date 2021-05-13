a,b=map(int,input().split())
if b==100:
  b+=1
for i in range(a):
  b*=100
print(b)