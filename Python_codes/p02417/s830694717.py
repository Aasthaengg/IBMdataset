s=[int(0) for i in range(26)]
while True:
    try:
        x=input()
        for i in range(len(list(x))):
            if 97<=ord(list(x)[i].lower())<=122:
                s[ord(list(x)[i].lower())-97]=s[ord(list(x)[i].lower())-97]+1
    except EOFError:
        break
for i in range(26):
    print(chr(97+i),":",s[i])