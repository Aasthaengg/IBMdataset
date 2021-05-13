N,S,p=int(input()),[],1
if N==0: print(0)
while N!=0:
    R=N%2
    S.append(R)
    N=(N-p*R)//2
    p*=-1
print(*reversed(S), sep="")