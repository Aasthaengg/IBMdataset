S=(input())
s=list(S)
K=int(input())
if K==1:
  print(s[0])
  exit()
for i in range(K):
  key=s[i]
  if key!='1':
    print(key)
    exit()
print(1)