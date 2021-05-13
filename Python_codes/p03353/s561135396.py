s=input()
k=int(input())
a=set()
for i in range(1,k+1):
  for j in range(len(s)-i+1):
    a|={s[j:j+i]}
print(sorted(a)[k-1])