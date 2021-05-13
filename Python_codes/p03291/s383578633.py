def main():
    S=input()
    N=len(S)
    abccounter=0
    abcounter=0
    acounter=0
    for i in range(0,N):
        if S[i]=='A':
            acounter+=1
        elif S[i]=='B':
            abcounter+=acounter
        elif S[i]=='C':
            abccounter+=abcounter
    hbccounter=0
    hbcounter=0
    hcounter=0
    for i in range(0,N):
        if S[i]=='?':
            hcounter+=1
        elif S[i]=='B':
            hbcounter+=hcounter
        elif S[i]=='C':
            hbccounter+=hbcounter
    ahccounter=0
    ahcounter=0
    acounter=0
    for i in range(0,N):
        if S[i]=='A':
            acounter+=1
        elif S[i]=='?':
            ahcounter+=acounter
        elif S[i]=='C':
            ahccounter+=ahcounter
    abhcounter=0
    abcounter=0
    acounter=0
    for i in range(0,N):
        if S[i]=='A':
            acounter+=1
        elif S[i]=='B':
            abcounter+=acounter
        elif S[i]=='?':
            abhcounter+=abcounter
    ahhcounter=0
    ahcounter=0
    acounter=0
    for i in range(0,N):
        if S[i]=='A':
            acounter+=1
        elif S[i]=='?':
            ahhcounter+=ahcounter
            ahcounter+=acounter
    hbhcounter=0
    hbcounter=0
    hcounter=0
    for i in range(0,N):
        if S[i]=='B':
            hbcounter+=hcounter
        elif S[i]=='?':
            hbhcounter+=hbcounter
            hcounter+=1
    hhccounter=0
    hhcounter=0
    hcounter=0
    for i in range(0,N):
        if S[i]=='C':
            hhccounter+=hhcounter
        elif S[i]=='?':
            hhcounter+=hcounter
            hcounter+=1
    Q=hcounter
    if Q>=3:
        ans=abccounter*3**Q+(hbccounter+ahccounter+abhcounter)*3**(Q-1)+(ahhcounter+hbhcounter+hhccounter)*3**(Q-2)+(Q*(Q-1)*(Q-2)//6)*3**(Q-3)
    elif Q==2:
        ans=abccounter*3**Q+(hbccounter+ahccounter+abhcounter)*3**(Q-1)+(ahhcounter+hbhcounter+hhccounter)*3**(Q-2)
    elif Q==1:
        ans=abccounter*3**Q+(hbccounter+ahccounter+abhcounter)*3**(Q-1)
    else:
        ans=abccounter*3**Q
    print(ans%(10**9+7))
if __name__ == '__main__':
    main()
