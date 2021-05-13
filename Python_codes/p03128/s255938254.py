l = [[0,0],[1,2],[2,5],[3,5],[4,4],[5,5],[6,6],[7,3],[8,7],[9,6]]
n,m = map(int,input().split())
a = list(map(int,input().split()))
l0 = []
for i in range(m):
    l0.append(l[a[i]])
l0.sort(key=lambda x:x[0],reverse=True)
l0.sort(key=lambda x:x[1])
p,q = l0[0]
count = n - (n//q)*q
c = 1
ans = 0
for i in range(n//q):
    ans += p*c
    c *= 10
c = c//10
l0.sort(key=lambda x:x[0],reverse=True)
i = 0
while count > 0 and i < m:
    p1,q1 = l0[i]
    if q1 > q:
        q1 -= q
    #print(count)
    if p1 > p:
        while count >= q1:
            ans -= p*c
            ans += p1*c
            count -= q1
            c = c//10
        i += 1
    else:
        i += 1
i = 0
c = 1
l0.sort(key=lambda x:x[1],reverse=True)
while count > 0 and i < m:
    p1,q1 = l0[i]
    if q1 > q:
        q1 -= q
    if p1 < p:
        while count >= q1:
            ans -= p*c
            ans += p1*c
            count -= q1
            c *= 10
        i += 1
    else:
        i += 1
if count == 0:
    print(ans)
else:
    x = n//q - 1
    for i in range(n//q-1):
        count = n - (x)*q
        c = 1
        ans = 0
        for i in range(x):
            ans += p*c
            c *= 10
        c = c//10
        l0.sort(key=lambda x:x[0],reverse=True)
        i = 0
        while count > 0 and i < m:
            p1,q1 = l0[i]
            if q1 > q:
                q1 -= q
            #print(count)
            if p1 > p:
                while count >= q1:
                    ans -= p*c
                    ans += p1*c
                    count -= q1
                    c = c//10
                i += 1
            else:
                i += 1
        i = 0
        c = 1
        l0.sort(key=lambda x:x[1],reverse=True)
        while count > 0 and i < m:
            p1,q1 = l0[i]
            if q1 > q:
                q1 -= q
            if p1 < p:
                while count >= q1:
                    ans -= p*c
                    ans += p1*c
                    count -= q1
                    c *= 10
                i += 1
            else:
                i += 1
        if count == 0:
            print(ans)
            break
        else:
            x += 1