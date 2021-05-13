s = list(map(str,input()))
t = list(map(str,input()))
for i in range(len(s)):
    if s[i]!=t[i]:
        print("No")
        break
    elif i+1==len(s):
        print("Yes")