s=int(input())
s=list(str(s))
k=int(input())
i=0
while True:
  if i==len(s):
    print(1)
    break
  if s[i]!="1":
    print(s[i])
    break
  else:
    i=i+1
  if i==k:
    print(1)
    break