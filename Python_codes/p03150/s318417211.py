s=input()
str1="keyence"
count=0
num=len(s)
if s==str1:
    yn=0
elif s[:7]==str1:
    yn=0
elif s[num-8:]==str1:
    yn=0
else:
    for i in range(7):
        if str1[i]==s[i]:
            count+=1
        else:
            break
    if s[num-7+count:]==str1[count:]:
        yn=0
    else:
        yn=1
if yn==0:
    print("YES")
else:
    print("NO")
