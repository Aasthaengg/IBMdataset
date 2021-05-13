S=input()

l=0
for i in range(len(S)):
  for j in range(i+1,len(S)+1):
    s = set(S[i:j])
    if s <= {'A','C','G','T'} and len(S[i:j])>l:
      l = len(S[i:j])
      
print(l)