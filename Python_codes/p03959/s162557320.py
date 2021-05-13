n = int(input())

al = list(map(int,input().split()))
tl = list(map(int,input().split()))


for i in range(n-1):
    if al[i] > al[i+1]:
        print(0)
        exit()
    if tl[i] < tl[i+1]:
        print(0)
        exit()

ans = 1
for i in range(n):
    a = False
    t = False
    if i != 0:
        if al[i] != al[i-1]:
            a = True
    else:
        a = True
    if i != n-1:
        if tl[i] != tl[i+1]:
            t = True
    else:
        t = True
    if a and t:
        if al[i] != tl[i]:
            print(0)
            exit()
    elif a:
        if al[i] > tl[i]:
            print(0)
            exit()
    elif t:
        if al[i] < tl[i]:
            print(0)
            exit()
    else:
        ans *= min(al[i], tl[i])
        ans %= 10**9 + 7

print(ans)




