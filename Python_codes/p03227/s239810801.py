S=input()

if (len(S)==2):
    print(S)

if (len(S)==3):
    temp=list(S)
    temp.reverse()
    print("".join(temp))