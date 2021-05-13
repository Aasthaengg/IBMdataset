s=str(input()[::-1])
word = ["maerd","esare","resare","remaerd"]
ans="YES"
i=0
while True:
    if i==len(s):
        break
    if s[i:i+5]==word[0]:
        i+=5
    elif s[i:i+5]==word[1]:
        i+=5
    elif s[i:i+6]==word[2]:
        i+=6
    elif s[i:i+7]==word[3]:
        i+=7
    else:
        ans="NO"
        break
print(ans)