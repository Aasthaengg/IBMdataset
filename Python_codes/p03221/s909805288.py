def nto6str(num):
    s =list('000000')
    numS = str(num)
    L_numS = len(numS)
    for i in range(L_numS):
        s[i*(-1)-1] = numS[i*(-1)-1]
    ans = ''.join(s)
    return ans

N,M =list(map(int,input().split()))
Lis = []
for i in range(M):
    a=list(map(int,input().split()))
    a.append(i)
    Lis.append(a)
b = sorted(Lis)
pref = 0
city = 0
for i in range(M):
    if b[i][0] != pref:
        pref = b[i][0]
        city = 1
    b[i][1] = city
    city +=1
for i in range(M):
    b[i][0] = nto6str(b[i][0])
    b[i][1] = nto6str(b[i][1])
c = sorted(b,key = lambda x:x[2])
for i in range(M):
    print(''.join(c[i][0:2]))
