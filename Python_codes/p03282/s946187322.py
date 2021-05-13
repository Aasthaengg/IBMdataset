s=input()
k=int(input())

notone=len(s)
for i in range(len(s)):
    if s[i]!="1":
        notone=i
        break
if notone>=k:
    print(1)
else:
    print(s[notone])