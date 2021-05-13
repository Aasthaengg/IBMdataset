mod = 10**9+7
S = list(input())
Thankyou = 1
DP=[]
#DP[x][y] x+1文字目までを見たときの、
#y=0,1,2 : A,AB,ABCの登場回数
if S[0] == "A" or S[0]=="?":
    DP.append([1,0,0])
    if S[0]=="?":
        Thankyou = 3
else:
    DP.append([0,0,0])
for i,s in enumerate(S):

    if i==0:continue
    a,b,c = DP[i-1]
    if s=="A":
        DP.append([(a+Thankyou)%mod,b,c])
    elif s=="B":
        DP.append([a,(a+b)%mod,c])
    elif s=="C":
        DP.append([a,b,(b+c)%mod])
    else:
        DP.append([(Thankyou+3*a)%mod,(a+3*b)%mod,(b+3*c)%mod])
        Thankyou *= 3
        Thankyou %= mod
print(DP[len(S)-1][2]%mod)