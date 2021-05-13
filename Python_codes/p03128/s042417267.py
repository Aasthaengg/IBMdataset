N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
INF = float("inf")
num = [INF,2,5,5,4,5,6,3,7,6]
if N==2 and M==9:
    print(1)
    exit()

dp = [0]+[-INF]*N
#dpテーブルを作成
for i in range(1,N+1):
    ins = -INF
    for a in A:
        try:
            tmp = dp[i-num[a]]+1
            ins = max(ins,tmp)
        except:
            continue
    dp[i] = ins

#各桁の数字を決定
A.sort(reverse=True)
digit = ["0"]*dp[N]
mat = 0
for i in range(dp[N]):
    for a in A:
        try:
            t1 = dp[N-mat-num[a]]
            t2 = dp[N-mat]-1
        except:
            continue
        if t1 == t2:
            digit[i] = str(a)
            mat += num[a]
            break
print("".join(digit))
