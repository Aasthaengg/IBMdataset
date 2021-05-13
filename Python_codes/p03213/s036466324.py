def wareru(n,k):
    res = 0
    for i in range(1,n):
        plus = n//(k**i)
        res+= plus
        if plus == 0:break
    return res
n = int(input())
prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
a = []
for p in prime :
    if wareru(n,p) > 1:
        a.append(wareru(n,p))
    else:break
cnt = [0]*5
for num in a:
    if num >= 74:
        cnt[0]+=1
    if num >= 24:
        cnt[1] +=1
    if num >= 14:
        cnt[2] += 1
    if num >= 4:
        cnt[3] += 1
    cnt[4]+= 1
ans = cnt[0]
ans += cnt[1]*(cnt[4]-1)
ans += cnt[2]*(cnt[3]-1)
ans += cnt[3]*(cnt[3]-1)*(cnt[4]-2)//2
print(ans)