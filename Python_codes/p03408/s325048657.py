n=int(input())
s=[input() for i in range(n)]
m=int(input())
t=[input() for i in range(m)]
dict={}

for i in s:
  if i not in dict.keys():
    dict[i]=1
  else:
    dict[i]+=1
for j in t:
  if j in s:
    dict[j]-=1
m=max(dict.values())
print(m if m>0 else "0")