def resolve():
    s=str(input())
    val=len(s)
    cntg=0
    cntp=0
    w=0
    l=0
    for i in range(len(s)):
        if cntg-cntp<=0:
            cntg+=1
            if s[i]=='p':
                l+=1
        else:
            if s[i]=='g':
                cntp+=1
                w+=1
            else:
                cntp+=1
    print(w-l)



resolve()