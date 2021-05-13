a=int(input())
li = list(map(int,input().split()))

ans = 'NO'

even = []
odd = []

for i in li:
  if i % 2 == 0:
    even.append(i)
  else:
    odd.append(i)

if len(odd) % 2 == 0:
  ans = 'YES'
  
print(ans)