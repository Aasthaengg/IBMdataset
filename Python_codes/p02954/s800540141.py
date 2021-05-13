S=input()
List1=[]
for i in range(len(S)-1):
  if S[i]=='R' and S[i+1]=='L':
    List1.append(i)
List2=[]
for i in range(len(S)-1):
  if S[i]=='L' and S[i+1]=='R':
    List2.append(i)
List2.append(len(S)-1)
ans=[0 for i in range(len(S))]
def f(a,b):
  g=(a+1)//2+b//2
  return g
for i in range(len(List1)):
  if i==0:
    a=List1[i]+1
    b=List2[i]-List1[i]
    ans[List1[i]]=f(a,b)
    ans[List1[i]+1]=a+b-f(a,b)
  else:  
    a=List1[i]-List2[i-1]
    b=List2[i]-List1[i]
    ans[List1[i]]=f(a,b)
    ans[List1[i]+1]=a+b-f(a,b)

print(*ans)