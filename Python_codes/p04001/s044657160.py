s = str(input())
l = len(s)
ans = 0
x = 2**(l-1)
dg = [[] for i in range(x)]
for i in range(x):
    b = 0#各桁の値
    d = 0#一つの値にするやつ
    tmp = 0 #数式計算用

    for j in range(l):
        b = int(s[j])
        d = d*10 +b
        if i>>j&1 :
            tmp += d
            dg[i].append(d)
            d = 0
    tmp += d
    ans += tmp
    dg[i].append(d)
# for i in range(x):
#     print(dg[i])
print(ans)

