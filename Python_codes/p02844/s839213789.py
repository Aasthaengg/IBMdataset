n=int(input())
s=input()
c=0
for i in range(10):
  a=s.find(str(i))
  if -1<a<n-2:
    
    for j in range(10):
      b=s[a+1:].find(str(j))
      if -1<b<len(s[a+1:])-1:
    
        for k in range(10):
          if s[a+b+2:].find(str(k))>-1:
            c+=1
print(c)