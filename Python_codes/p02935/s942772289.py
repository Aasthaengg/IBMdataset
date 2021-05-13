n=int(input())
l=sorted(list(map(int,input().split())))

num=(l[0]+l[1])/2
l.pop(0)
l.pop(0)
if len(l) > 0:
  for i in range(n-2):
    num=(num+l[0])/2
    l.pop(0)
  
print(num)