n,k = map(int,input().split())
X = [int(i) for i in input().split()]
ans = 10**9

for i in range(n-k+1):
    Max = X[i+k-1]
    Min = X[i]
    
    if Max<0 and Min<0:
        tmp_ans = abs(Min)
    elif Max>0 and Min >0:
        tmp_ans = abs(Max)
    else:
        tmp_ans = abs(Max) + abs(Min) + min(abs(Max),abs(Min))
    ans = min(ans,tmp_ans)
print(ans)