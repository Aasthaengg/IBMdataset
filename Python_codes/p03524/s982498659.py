from collections import Counter

c=Counter(input())
l=sorted([c["a"],c["b"],c["c"]])

if l[0]==l[1]==0:print("YES" if l[2]==1 else "NO");exit()
if l[0]==0:print("YES" if l[1]==l[2]==1 else "NO");exit()
if l[0]==l[1]==l[2]:print("YES")
elif l[0]+1==l[1]==l[2]:print("YES")
elif l[0]+1==l[1]+1==l[2]:print("YES")
else:print("NO")