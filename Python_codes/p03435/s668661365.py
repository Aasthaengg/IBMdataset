[a,b,c]=[int(i) for i in input().split()]
[d,e,f]=[int(j) for j in input().split()]
[g,h,i]=[int(k) for k in input().split()]
t=0
if d-a == e-b and e-b == f-c:
  t+=1
if g-d == h-e and h-e == i-f:
  t+=1
if b-a == e-d and e-d == h-g:
  t+=1
if c-b == f-e and f-e == i-h:
  t+=1
if t== 4:
  print("Yes")
else:
  print("No")