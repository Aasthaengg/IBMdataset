N = int(input())
S = sorted(int(input()) for T in range(0,N))
MAX = sum(S)
if MAX%10==0:
    R10 = [T for T in S if T%10!=0]
    if len(R10)==0:
        print(0)
    else:
        print(MAX-R10[0])
else:
    print(MAX)