A,B,C = list(map(int,input().split()))
if A == B == C and A%2 == 0 :
    print(-1)
elif A == B == C and A%2 == 1 :
    print(0)
else :
    cnt=0
    while A%2==B%2==C%2==0:
        total=A+B+C
        A=total//2-A//2
        B=total//2-B//2
        C=total//2-C//2
        cnt+=1
    print(cnt)
