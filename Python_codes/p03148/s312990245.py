from collections import*
n,k=map(int,input().split())
sushi=sorted([tuple(map(int,input().split()))for i in range(n)],key=lambda x:x[1],reverse=1)
first=defaultdict(list)
second=defaultdict(list)
menu=set()

for _,v in sushi[:k]:
    menu.add(_)
    first[_].append(v)
second=sushi[k:][::-1]
score=sum(map(sum,first.values()))
change=[]
for _,v in first.items():
    for i in v[1:]:
        change.append((_,i))
change.sort(key=lambda x:x[1],reverse=1)

#print(first,change,second)
ans=[score+len(first)**2]
while change and second:
    _,s=change.pop()
    score-=s
    try:
        while second[-1][0] in menu:
            pp,ss=second.pop()
        pp,ss=second.pop()
        menu.add(pp)
        score+=ss
        ans.append(score+len(menu)**2)
    except:
        break
print(max(ans))

