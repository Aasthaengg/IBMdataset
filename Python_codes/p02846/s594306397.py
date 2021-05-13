T1,T2 = map(int,input().split())
A1,A2 = map(int,input().split())
B1,B2 = map(int,input().split())

C1,C2 = B1-A1, B2-A2

if C1 > 0:
    if C1*T1+C2*T2 > 0:
        ans = 0
    elif C1*T1+C2*T2 == 0:
        ans = 'infinity'
    else:
        d = abs(C1*T1+C2*T2)
        if C1*T1%d==0:
            ans = 2*C1*T1//d
        else:
            ans = 2*(C1*T1//d)+1
else:
    if C1*T1+C2*T2 < 0:
        ans = 0
    elif C1*T1+C2*T2 == 0:
        ans = 'infinity'
    else:
        d = abs(C1*T1+C2*T2)
        dd = abs(C1*T1)
        if dd%d==0:
            ans = 2*dd//d
        else:
            ans = 2*(dd//d)+1
        
print(ans)