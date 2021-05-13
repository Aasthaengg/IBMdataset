N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
anum=0
bnum=0
equalflag=0
for i in range(N):
    if a[i]>b[i]:   #bを嵩上げしないと
        bnum=bnum+(a[i]-b[i])
    elif a[i]<b[i]:#aを嵩上げしないと
        if (b[i]-a[i])%2==0:    #差が2nならaをn回嵩上げ
            anum=anum+(b[i]-a[i])//2
        else:                   #差が2n+1ならbを一回嵩上げしてからaをn+1回嵩上げ
            bnum=bnum+1
            anum=anum+((b[i]+1)-a[i])//2
if N!=1:
    if anum>=bnum:
        print("Yes")
    else:
        print("No")
else:
    if anum==bnum:
        print("Yes")
    else:
        print("No")