n=int(input())
l=[]
for i in range(n):
  a,b=list(map(int,input().split()))
  l.append(int(a==b))
for i in range(n-2):
  if l[i] and l[i+1] and l[i+2]:
    print("Yes")
    break
else:
  print("No")