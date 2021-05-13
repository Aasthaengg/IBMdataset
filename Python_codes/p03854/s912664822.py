s = input()
s=s[::-1]
i=0
ans="YES"
while True:
    if len(s)==i:
        break
    elif s[i:i+5]=="maerd":
        i+=5
    elif s[i:i+7]=="remaerd":
        i+=7
    elif s[i:i+5]=='esare':
        i+=5
    elif s[i:i+6]=='resare':
        i+=6
    else:
        ans="NO"
        break
print(ans)