n, m, x = map(int, input().split())

#金額と理解度のリスト
money = []
skill = []
for i in range(n) :
    a = []
    a = (list(map(int, input().split())))
    money.append(a[0])
    skill.append(a[1:])

#本の購入パターン
l_list = []
for j in range(2 ** n) :
    l = []
    for k in range(n) :
        if (j >> k) & 1 :
            l.append(1)
        else:
            l.append(0)
        
    l_list.append(l)

#金額と理解度の合計のリスト
ans = -1
min_money_sum = sum(money)
for o in l_list :
    ability = [0 for s in range(m)]
    money_sum = 0
    for p in range(n) :
        if o[p] == 1 :
            ability = [q + r for (q, r) in zip(ability, skill[p])]
            money_sum += money[p]
    
    cnt = 0 
    for t in range(m) :
        if ability[t] < x :
            cnt += 1
    
    if cnt == 0 :
        min_money_sum = min(min_money_sum, money_sum)
        ans = 0

#最小額
if ans != -1 :
    print(min_money_sum)
else:
    print(ans)