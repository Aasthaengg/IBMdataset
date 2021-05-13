icase=46    
if icase==46:
    a=list(map(int,input().split()))
    icnt=1
    if a[0]!=a[1]:
        icnt=icnt+1
    if a[0]!=a[2] and  a[1]!=a[2]:
        icnt=icnt+1
    print(icnt)