s = input()
t = input()
cont=0

for i in range(len(s)):
    if s[i] != t[i]: cont+=1
    
if cont == 0 and len(s)+1==len(t): print("Yes")
else: print("No")
