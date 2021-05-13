s=input()
n=len(s)
cnt=0
p=s[0]
for i in range(n):
  if p!= s[i]:
    cnt+=1
  p=s[i]
print(cnt)