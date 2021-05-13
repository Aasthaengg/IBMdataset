n,m = map(int,input().split())
p = [list(map(str,input().split())) for _ in range(m)]
###ACとWAのフラグを作成、ACしたらフラグを立てていく
ac =[0]*(n+1)
wa =[0]*(n+1)
for i in range(m):
    question =int(p[i][0])
    ###フラグが立っていればカウントしない
    if p[i][1] == "AC" and ac[question] == 0:
        ac[question] = 1
     ###同様に一度ACしてフラグがあるならWAもカウントしない
    elif p[i][1] == "WA" and ac[question] == 0:
        wa[question] += 1
for j in range(n+1):
  ###ACしていないならばWAはカウントしない
    if ac[j] == 0:
        wa[j] = 0
       # print(wa)
print(sum(ac),sum(wa))
