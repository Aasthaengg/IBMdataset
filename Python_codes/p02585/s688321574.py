n,k=map(int,input().split())

p=list(map(int,input().split()))
score=list(map(int,input().split()))

group_score=[]
checked=[0]*n

for i in range(n):
    if checked[i]==0:
        tmp_group=[]
        tmp=i
        while checked[tmp]==0:
            checked[tmp]=1
            tmp_group.append(score[tmp])
            tmp=p[tmp]-1
        group_score.append(tmp_group)



#aryの中から連続するk個選択するときの最大
def calc(k):
    if k==0:
        return 0
    global group
    ans="INF"
    for i in range(len(group)):
        tmp=0
        for j in range(k):
            tmp+=group[(i+j)%len(group)]
            if ans=="INF":
                ans=tmp
            else:
                if ans<tmp:
                    ans=tmp
    return ans

ans=score[0]
for group in group_score:
    #一周以上する場合
    if len(group)<k:
        cycle=sum(group)
        if cycle>0:
            cycle_sum=cycle*(k//len(group))
            tmp=calc(k%len(group))
            ans=max(ans,cycle_sum+tmp)

            if k//len(group)>=2:
                cycle_sum=cycle*(k//len(group)-1)
                tmp=calc(len(group))
                ans=max(ans,cycle_sum+tmp)
          

        tmp=calc(len(group))
        ans=max(ans,tmp)



    #一周しない場合k)
    else:
        tmp=calc(k)
        ans=max(ans,tmp)

print(ans)