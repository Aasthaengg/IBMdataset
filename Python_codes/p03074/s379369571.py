N, K = map(int,input().split())
S = input()

#圧縮（正の数が直立，負の数が逆立ち）
people = []
tmp = 0
for s in S:
    if s == "0":#直立
        if tmp >= 0:
            tmp += 1
        else:
            people.append(tmp)
            tmp = 1
    else:#逆立ち
        if tmp <= 0:
            tmp -= 1
        else:
            people.append(tmp)
            tmp = -1
people.append(tmp)

#print(people)

rev = 0#反転回数
ans = 0
#初めの範囲で
for i,num in enumerate(people):
    if num < 0:#元から逆立ちの時
        ans += -num
    else:
        rev += 1
        ans += num
    if rev == K:#それ以上反転できないので，右隣の逆立ち(居れば)の分だけ足して終わる
        try:
            ans += -people[i+1]
            break
        except IndexError:#最後に足した逆立ち群がそもそも右端だったら
            break

#print("initial ans",ans)

#SlidingWindow 右端と左端
right = (i+1)+1
left = 0

tmp = ans
#SlidingWindow
while True:
    #左端の更新
    if people[left] < 0:
        tmp -= abs(people[left])
        try:
            tmp -= abs(people[left+1])
            left += 2
        except IndexError:#len(people)==1のときだけ
            break
    else:
        tmp -= abs(people[left])
        left += 1
    
    #右端の更新
    try:
        tmp += abs(people[right])
        right += 1
    except IndexError:
        break
    
    try:
        tmp += abs(people[right])
        right += 1
    except IndexError:
        break
    ans = max(tmp, ans)

ans = max(tmp, ans)
print(ans)