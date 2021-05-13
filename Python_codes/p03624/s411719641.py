s=input()
A=[False]*26
for i in range(len(s)):
    A[ord(s[i])-97]=True
for i in range(26):
    if A[i]==False:
        print(chr(i+97))
        break
else:
    print("None")