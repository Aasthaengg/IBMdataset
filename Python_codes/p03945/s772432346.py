s=input()
t=[]
for i in range(len(s)-1):
  if s[i]!=s[i+1]:
    t.append(s[i])
t.append(s[-1])
print(len(t)-1)