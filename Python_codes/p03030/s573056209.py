n=int(input())

l=[]
for i in range(n):
  s,p=input().split()
  p=-int(p)
  l.append([s,p,i+1])

l.sort()
for i in l:
  print(i[-1])