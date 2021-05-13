n=int(input())
a=[int(input()) for i in range(n)]

l1=sorted(a)[-1]
l2=sorted(a)[-2]

for i in a:
  if i==l1:
    print(l2)
  if i!=l1:
    print(l1)