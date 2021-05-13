n=int(input())
l=[]
for i in range(n):
  a=int(input())
  l.append(a)
l[l.index(max(l))]=l[l.index(max(l))]//2
print(sum(l))