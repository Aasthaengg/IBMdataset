s=input()
n=len(s)
m=(n-1)//2
t=s[:m]

for i in range(m):
  #print(s[i],s[-i-1])
  if s[i]!=s[-i-1]:
    print('No')
    exit()
if m%2==1: l=(m-1)//2
else: l=m//2
for i in range(l):
  #print(t[i],t[-i-1])
  if t[i]!=t[-i-1]:
    print('No')
    exit()
print('Yes')