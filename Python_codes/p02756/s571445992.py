S=input()
# Python3 program to Split string into characters 
def split(word): 
    return [char for char in word]  
word = S
splits=split(S)
Q=int(input())
flipcounter=0
prestring=[]
poststring=[]
for i in range(0,Q):
  inputforround=input()
  if inputforround=='1':
    flipcounter=flipcounter+1
  else:
    T,F,C=map(str,inputforround.split())
    if (int(F)+flipcounter)%2==1:
      prestring.append(C)
    else:
      poststring.append(C)
prestring.reverse()
for j in splits:
  prestring.append(j)
for k in poststring:
  prestring.append(k)
if flipcounter%2==1:
  prestring.reverse()
ans=''.join(prestring)
print(ans)
