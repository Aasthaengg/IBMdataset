N=int(input())
S=input()
use=[0 if S[i]=="." else 1 for i in range(N)]
now=[0 for i in range(N)]
count=sum(use)
lst=set()
lst.add(count)


for i in range(N-1,-1,-1):
    now[i]=1
    if use[i]:
        use[i]=0
        count-=1
    else:
        use[i]=1
        count+=1
    lst.add(count)
print(min(lst))
