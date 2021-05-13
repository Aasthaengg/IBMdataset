X=input()
N=len(X)
stack=[]
ans=0

for i in range(N):
  if X[i]=="S":
    stack.append(X[i])
  else:
    if len(stack)>0:
      stack.pop()
    else:
      ans += 1
ans += len(stack)

print(ans)