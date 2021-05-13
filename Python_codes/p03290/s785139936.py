import itertools

D,G = list(map(int,input().split()))
PC = []
for i in range(D):
    PC.append(list(map(int,input().split())))

#ボーナスをどの問題でもらうか
#bonus=[0]*D

a = [0,1]
Ls = list(itertools.product(a, repeat=D))

#最大数 更新していく
out=1000

for L in Ls:
    count=0
    score=0

    for i in range(D):
        if L[i]==1:
            count+=PC[i][0]
            score+=100*(i+1)*PC[i][0]
            score+=PC[i][1]

    hanpa = D-1
    while (L[hanpa]==1) and (hanpa>=0):
        hanpa-=1
    if hanpa==-1:
        cnt=0
    else:
        cnt=0
        while (score<G) and (cnt<PC[hanpa][0]):
            cnt+=1
            count+=1
            score+=(hanpa+1)*100
    if (score>=G) and (count<out):
        out=count
print(out)