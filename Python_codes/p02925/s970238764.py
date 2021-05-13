n=int(input())

battle=[]

def mainasu(x):
    return int(x)-1

front=[]

for _ in range(n):
    tmp=list(map(mainasu,input().split()))[::-1]
    front.append(tmp.pop())
    battle.append(tmp)

def pri():
    global front,battle,day,checkday
    print(day,front,battle,checkday)

day=0

checkday=[-1]*n

#pri()
cnt=0
while 1:
    flag=0
    for i in range(n):
        if i<n and front[i]<n and i==front[front[i]] and checkday[i]<day and checkday[front[i]]<day:
            flag=1
            if len(battle[front[i]])>0:
                front[front[i]]=battle[front[i]].pop()
                checkday[front[i]]=day
            else:
                front[front[i]]=n
                cnt+=1
            
            if len(battle[i])>0:
                front[i]=battle[i].pop()
                checkday[i]=day
            else:
                front[i]=n
                cnt+=1
    #pri()
    if flag==0:
        break
    
    day+=1


if cnt==n:
    print(day)
else:
    print(-1)            

    


