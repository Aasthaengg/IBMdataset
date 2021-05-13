s,t=input(),input()

s+=s

for i in range(len(t)):
    if t==s[i:len(t)+i]:print("Yes");break
else:print("No")