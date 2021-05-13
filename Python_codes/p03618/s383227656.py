s=input()
l={}
for i in s:
  if i in l:
    l[i]+=1
  else:
    l[i]=1

def c(x):
  return x*(x-1)//2

sm=c(len(s))
for i in l:
  sm-=c(l[i])
print(sm+1)