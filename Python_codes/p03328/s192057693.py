a,b=list(map(int, input().split()))
s=0
for i in range(b-a-1):
  s+=i+1
print(s-a)