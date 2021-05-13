S=input()
A="abcdefghijklmnopqrstuvwxyz"
ans=100
for a in A:
  T=S;
  x=0;
  while(T.count(a)!=len(T)):
    U=""
    for i in range(len(T)-1):
      U+=(T[i+1]if T[i+1]==a else T[i])
    T=U
    x+=1
  ans=min(ans,x)
print(ans)