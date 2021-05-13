s=input()
t=input()
ar1=[0]*26
ar2=[0]*26
for i in s:
    ar1[ord(i)-97]+=1
for i in t:
    ar2[ord(i)-97]+=1
ar1.sort()
ar2.sort()
if ar1==ar2:
    print("Yes")
else:
    print("No")