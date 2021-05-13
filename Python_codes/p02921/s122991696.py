icase=0
if icase==0:
    s=list(input())
    t=list(input())
    icnt=0
    for i in range(3):
        if s[i]==t[i]:
            icnt=icnt+1
    print(icnt)