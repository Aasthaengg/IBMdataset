a=input()
a=a.replace("BC","X")
a=a[::-1]
X_c=0
ans=0
for i in range(len(a)):
   if a[i]=="X":
      X_c+=1
   elif a[i]=="A":
      ans+=X_c
   else:
      X_c=0
print(ans)