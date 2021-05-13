def main():
    N,C=map(int,input().split())
    stc=[0]*N
    for i in range(N):
        abc=list(map(int,input().split()))
        stc[i]=abc

    a=[0]*(C+1)
    stc.sort(key=lambda x:(x[2],x[0]))
    c=1
    for i in range(N):
        while stc[i][2]!=c:
            c+=1
        if stc[i][2]==c:
            a[c]+=1
    for i in range(1,C+1):
        a[i]+=a[i-1]
    
    table=[0]*(2*10**5+2)
    for i in range(C):
        for j in range(a[i],a[i+1]):
            if j==a[i]:
                table[stc[j][0]*2-1]+=1
                table[stc[j][1]*2]-=1
            else:
                if stc[j-1][1]==stc[j][0]:
                    table[stc[j][0]*2]+=1
                    table[stc[j][1]*2]-=1
                else:
                    table[stc[j][0]*2-1]+=1
                    table[stc[j][1]*2]-=1                    
    M=0
    for i in range(len(table)):
        if 0<i:
            table[i]+=table[i-1]
    for i in range(len(table)):
        if M<table[i]:
            M=table[i]
    print(M)
if __name__=="__main__":
    main()