n=int(input())

l=[x for x in range(1,n+1)]

p=0

for ll in l:
  if ll%2!=0:
    p+=1

print(p/len(l))