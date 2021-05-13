from collections import Counter
n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
cou=Counter(a).most_common()
rem=len(cou)-k
i=-1
ans=0
while rem>0:
    ans+=cou[i][1]
    i-=1
    rem-=1;
print(ans)