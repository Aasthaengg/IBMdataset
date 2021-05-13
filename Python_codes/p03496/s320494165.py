n=int(input())
a = list(map(int,input().split()))

s = max(a)
t = min(a)

if s == t:
    print(0)
elif abs(s) > abs(t):
    ss = a.index(s)
    print(2*n-2)
    for i in range(0,n):
        if i != ss:
            print(str(ss+1) + ' ' + str(i+1))
    for i in range(1,n):
        print(str(i) + ' '+str(i+1))
else:
    tt = a.index(t)
    print(2*n-2)
    for i in range(n):
        if i != tt:
            print(str(tt+1) + ' ' + str(i+1))
    for i in range(1,n):
        print(str(n-i+1) + ' ' + str(n-i))