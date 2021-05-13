s=input()
k=int(input())
c=0
for i in range(len(s)):
    if s[i]=="1":
        c+=1
    else:
        break
if k<=c:
    print("1")
else:
    print(s[c])