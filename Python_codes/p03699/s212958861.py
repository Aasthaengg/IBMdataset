N=int(input())
F=False

S=[]
for _ in range(N):
    s=int(input())
    S.append(s)
    F|=(s%10!=0)

if not F:
    print(0)
else:
    if sum(S)%10:
        print(sum(S))
    else:
        x=float("inf")
        for s in S:
            if s%10!=0 and x>s:
                x=s
        print(sum(S)-x)
