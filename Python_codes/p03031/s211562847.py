n,m = map(int,input().split())
dic = {}
for i in range(m):
    s = list(map(int,input().split()))[1:]
    dic[i] = s
P = list(map(int,input().split()))
# print(dic)

ans = 0

# ON/OFFをbit全探索
for i in range(2**n):
    on_off = [False]*n
    for j in range(n):
        if ((i>>j)&1):
            on_off[j] = True
    flag = True
    for k in range(m):
        cnt = 0
        for l in dic[k]:
            if on_off[l-1]:
                cnt += 1
        if cnt % 2 != P[k]:
            flag = False
    if flag:
        ans += 1
print(ans)