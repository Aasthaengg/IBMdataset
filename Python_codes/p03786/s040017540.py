n=int(input())
a=list(map(int,input().split()))
a.sort()
size=a[0]
num=1
for i in a[1:]:
  if size*2>=i:
    num+=1
  else:
    num=1
  size+=i
print(num) 