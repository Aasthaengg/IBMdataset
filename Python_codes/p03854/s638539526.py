s0=input()
s1="maerd"
s2="remaerd"
s3="esare"
s4="resare"
s=""
for i in range(len(s0)):
    s+=s0[-1-i]
num=0
num2=len(s)
ans=0
for i in range(num2):
    if num==num2:
        ans=1
        break
    if num2-num<=4:
        break
    if num2-num<=7:
        s13=s[num:]
        if s13==s1 or s13==s2 or s13==s3 or s13==s4:
            ans=1
        break
    if s[num:num+5]==s1 or s[num:num+5]==s3:
        num+=5
    elif s[num:num+6]==s4:
        num+=6
    elif s[num:num+7]==s2:
        num+=7
    else:
        break
if ans==0:
    print("NO")
else:
    print("YES")
