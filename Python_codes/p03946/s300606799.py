n,t = map(int, input().split( ))
a = list(map(int, input().split( )))
mn = 10**10
mx = 0
cnt_mn = 0#現在の買値の最小値
cnt_inf = 0#最大りえきの達成で買える町の数
cnt_sup = 0#現在の最大利益の達成で売れる町の数
for i in range(n):
    if a[i]<mn:
        mn = a[i]
        cnt_mn = 1
    elif a[i] == cnt_mn:
        cnt_mn += 1
    if mx < a[i] - mn:
        mx = a[i] - mn
        cnt_sup = 1
        cnt_inf = cnt_mn
    elif mx == a[i]-mn:
        cnt_sup += 1
        cnt_inf += cnt_mn

print(min(cnt_inf,cnt_sup))