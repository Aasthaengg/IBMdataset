s=input()
s_l=len(s)

left=[0 for i in range(s_l+1)]
right=[0 for i in range(s_l+1)]

for i in range(s_l):
  if s[i]=='<':
    left[i+1]=left[i]+1
for i in range(s_l-1,-1,-1):
  if s[i]=='>':
    right[i]=right[i+1]+1

ans=0
for i,j in zip(left,right):
  ans+=max(i,j)
print(ans)