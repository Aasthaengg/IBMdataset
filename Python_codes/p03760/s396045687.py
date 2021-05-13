s=input()
t=input()

l=""
i=0
j=0
while True:
  if i < len(s):
    l+=s[i]
    i+=1
  if j < len(t):
    l+=t[j]
    j+=1
  if len(l) == len(s)+len(t):
    break
print(l)
