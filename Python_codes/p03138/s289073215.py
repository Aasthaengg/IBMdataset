n,k=map(int,input().split())
A=list(map(int,input().split()))
m=max(k,max(A))
l=len(bin(m))-2
C=[0]*l
for a in A:
    for i in range(l):
        if (a>>i)&1:
            C[-i-1]+=1
One=[] #答えを1にしたときに貰える値
Zero=[] #0にしたとき
for i in range(l):
    One.append(2**(l-i-1)*(n-C[i]))
    Zero.append(2**(l-i-1)*C[i])

b=bin(k)[2:]
lb=len(b)

cnt=0
if lb<l: #Kの左端より左は全部0
    cnt=sum(Zero[:(l-lb)])
dp1=[One[l-lb]] #i桁目までKと一致しているときの最大値
dp2=[Zero[l-lb]] #i桁目まででKより小さいときの最大値

for i in range(1,lb):
    a1=One[l-lb+i]
    a0=Zero[l-lb+i]
    if b[i]=="1":
        dp1.append(dp1[-1]+a1)
        dp2.append(max(dp1[-2]+a0,dp2[-1]+max(a1,a0)))
    else:
        dp1.append(dp1[-1]+a0)
        dp2.append(dp2[-1]+max(a1,a0))

if k==0:
    print(cnt+dp2[0])
else:
    print(cnt+max(dp1[-1],dp2[-1]))