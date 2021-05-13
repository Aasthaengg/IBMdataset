s=input()
k=int(input())
t=set()
for i in range(1,min(k,len(s))+1):
  for j in range(len(s)-i+1):
    t.add(s[j:j+i])
t=list(t)
t.sort()
print(t[k-1])