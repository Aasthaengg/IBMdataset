n,l=map(int,input().split())
apple=list(range(1,n+1))
aji=[l+i-1 for i in apple]
sum_num=sum(aji)
sa=10000
for i in range(len(aji)):
    if abs(aji[i])<sa:
        sa=abs(aji[i])
        ans=aji[i]
print(sum_num-ans)