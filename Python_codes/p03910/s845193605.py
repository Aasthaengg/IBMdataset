n=int(input())
s=set()
current=1
cusum=0
while cusum<n:
  cusum+=current
  s.add(current)
  current+=1
if cusum-n in s:
  s.remove(cusum-n)
for i in s:
  print(i)