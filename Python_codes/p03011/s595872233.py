try:
    n=list(map(int, input().strip().split()))
    lis1=[]
    for i in range(0,len(n)):
        for a in range(0,len(n)):
            if a!=i:
                z=(int(n[a])+int(n[i]))
                lis1.append(z)
            
    minscore='9999999999'
    for i in range(0,len(lis1)):
        if float(minscore)>float(lis1[i]):
            minscore=lis1[i]
    
    print(minscore)
    
except:
    print('')

