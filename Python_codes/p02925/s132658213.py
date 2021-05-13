#https://qiita.com/vain0x/items/fbde8b66927b84080811
#http://kmjp.hatenablog.jp/entry/2019/09/01/1000
#2人の選手が互いに相手を次の対戦相手に指定しているとき以外組めない
#したがって貪欲で一意

n = int(input())
a = []

for i in range(n):
    ai = list(map(int, input().split( )))
    ai.reverse()
    for j in range(n-1):
        ai[j]-=1
    a.append(ai)

##キューの管理のどこがおかしいかわからなかったがあきらめる

can={i for i in range(n)}
nxt=set()
cnt = 0
rem=n*(n-1)//2
while rem:
    cnt+=1
    for i in can:
        if i not in nxt and a[i]:
            p = a[i][-1]
            if p not in nxt:##この判定しないと1日に複数回試合することになる
                if a[p][-1]==i:
                    a[p].pop();a[i].pop()
                    nxt.add(i);nxt.add(p)
    rem-=len(nxt)//2

    can=nxt.copy()###copy
    nxt=set()
    if not can:
        break
       
if rem:
    print(-1)
else:       
    print(cnt)
        
        
        
