import itertools
n=int(input())
a=list(map(int,input().split()))
cumsum=[0]+list(itertools.accumulate(a))
sum_num=sum(a)
ans=10**100
for i in range(1,n):
    yen=abs(cumsum[i]-(sum_num-cumsum[i]))
    if yen<ans:
        ans=yen
print(ans)