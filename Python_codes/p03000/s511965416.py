N,X = map(int, input().split())
L = list(map(int, input().split()))
p=0
c=1
for l in L:
  p+=l
  if p <= X:
    c+=1
  else:
    break
print(c)