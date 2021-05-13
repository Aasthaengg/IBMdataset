s=input()[::-1]
a="dream"[::-1]
b="dreamer"[::-1]
c="erase"[::-1]
d="eraser"[::-1]
i=0
ans="YES"
while i<len(s):
    if a in s[i:i+5]:
        i+=5
    elif b in s[i:i+7]:
        i+=7
    elif c in s[i:i+5]:
        i+=5
    elif d in s[i:i+6]:
        i+=6
    else :
        ans="NO"
        break

print(ans)