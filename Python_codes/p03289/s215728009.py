S=list(map(lambda x:x,input()))

F=(S[0]=="A")
F&=(S[2:-1].count("C")==1)

if F:
    S.remove("A")
    S.remove("C")
    for s in S:
        F&=(s==s.lower())
if F:
    print("AC")
else:
    print("WA")
