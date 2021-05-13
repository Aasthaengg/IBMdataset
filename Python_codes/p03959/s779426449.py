n = int(input())
Ts = list(map(int, input().split()))
As = list(map(int, input().split()))

prev = 0
inds = []
for t in Ts:
    if prev < t:
        inds.append((t,1))
    else:
        inds.append((t,0))
    prev = t
indsA = []
prev = 0
for a in As[::-1]:
    if prev < a:
        indsA.append((a,1))
    else:
        indsA.append((a,0))
    prev = a
# print(inds, indsA[::-1])
# if Ts[-1] != As[0]:
#     print(0)
#     exit()
ans = 1
MOD = 10**9 + 7
for it, ia in zip(inds, indsA[::-1]):
    # print(it,ia)
    if it[1] == 1 and ia[1] == 1:
        if it[0] != ia[0]:
            # 矛盾
            print(0)
            exit()
    elif it[1] == 1 and ia[1] == 0:
        # print("t",it,ia)
        if it[0] > ia[0]:
            print(0)
            exit()
    elif it[1] == 0 and ia[1] == 1:
        # print("a",it,ia)
        if it[0] < ia[0]:
            print(0)
            exit()
    else:
        mn = min(it[0],ia[0])
        ans *= mn
        ans %= MOD
    # print(it,ia,ans)
print(ans)
