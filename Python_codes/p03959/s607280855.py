n = int(input())
qs1 = list(map(int,input().split(" ")))
qs2 = list(map(int,input().split(" ")))
qs2.reverse()
ans = 1
MOD = 10** 9 + 7
num1 = 0
num2  = 0
qss = [[],[]]
for i,qs in enumerate([qs1,qs2]):
    qss[i].append((qs[0], 1))
    for t1,t2 in zip(qs[0:n-1],qs[1:n]):
        if t1 >t2:
            ans *= 0
        elif t1 == t2:
            qss[i].append((t2,0))
        else:
            qss[i].append((t2, 1))
# print(qss)
qss[1].reverse()
# print(qss)
for q1,q2 in zip(qss[0],qss[1]):
    qt1 = q1[1]
    qt2 = q2[1]
    num1 = q1[0]
    num2 = q2[0]
    if qt1 == 0 and qt2 == 0: #
        ans *= min(num1, num2)


    elif qt1 == 0 and qt2 == 1:
        if num1 >= num2:
            ans *= 1
        else:
            ans *= 0

    elif qt1 == 1 and qt2 == 0:
        if num2 >= num1:
            ans *= 1
        else:
            ans *= 0
    else:
        if num1 != num2:
            ans *= 0
    ans %= MOD
print(ans)