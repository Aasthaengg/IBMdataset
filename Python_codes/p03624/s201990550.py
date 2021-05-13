s=input()
S=[]
count=0
for i in range(len(s)):
    S.append(s[i])
for x in range(26):
    if chr(x+ord("a")) in S:
        count=count+1
    else:
        print(chr(x+ord("a")))
        break
if count==26:
    print(None)
else:
    pass