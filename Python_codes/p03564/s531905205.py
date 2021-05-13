n = int(input())
k = int(input())
tmp = 1

while n>0:
  if tmp*2>(tmp+k):
    tmp +=k
  else:
    tmp *=2
  n -= 1
    
print(tmp)