n=int(input())
s=list(input())
ma=0
for i in range(n):
  c=[]
  count=0
  a=s[:i+1]
  b=s[i+1:]
  for j in range(len(a)):
    if a[j] not in c:
      if a[j] in b:
        c.append(a[j])
        count+=1
    if count>ma:
      ma=count
print(ma)