# solution

data=int(input())
M=10**9+7

dp={b:1 for b in 'ACGT'}
for i in range(data-1):
    dp_next={}
    for j in dp:
        for k in 'AGCT':
            elem=j[-3:]+k
            if elem[-3:] in ('AGC','GAC','ACG') or elem in ('AGGC','ATGC','ACGC','AGTC','AGGC'):
                continue
            else:
                dp_next.setdefault(elem,0)
                dp_next[elem]+=dp[j]
    dp=dp_next
print(sum(dp.values())%M)