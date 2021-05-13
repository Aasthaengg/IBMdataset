n,c,k = map(int,input().split())
t = []
for i in range(n):
    t.append(int(input()))
    
t = sorted(t)
bus = []
ans = 1
for i in range(n):
    if len(bus) < c: #バスの定員に余裕があるとき
        if not bus:#バスに誰も乗っていなかったらバスに人を乗せる
            bus.append(t[i])
        elif t[i] <= bus[0] + k:#バスに初めて人が乗った時刻にkを足して、それよりt[i]が小さければバスに乗せる
            bus.append(t[i])
        else:#上記のelifを満たさない場合
            ans +=1
            bus = []
            bus.append(t[i])
    elif len(bus) == c:
        ans +=1
        bus = []
        bus.append(t[i])
    else:
        ans +=1
        bus = []
print(ans)