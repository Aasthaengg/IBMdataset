w=list(input())
n=len(w)
S=0
S_max=S
for i in range(n):
  if w[i]=='R':
    S+=1
    j=0
    while True:
      if i+j+1<=n-1:
        j+=1
        if w[i+j]=='R':
          S+=1
        else:
          i+=j
          break
      else:
        i=n-1
        break
  S_max=max([S_max,S])
  S=0
print(S_max)