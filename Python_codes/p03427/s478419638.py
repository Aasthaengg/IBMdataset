N=int(input())
S=str(N)
if len(S)==1:
  print(N)
  exit()
a=int(S[0])
b=len(S)
N=a+((b-1)*9)-1
if int(S[1:])==(10**(b-1))-1:
  N+=1
print(N)