s = input()
n = len(s)

ans = 0
for i in range(2**(n-1)):
    c = 10
    tmp = int(s)
    res = 0
    for j in range(n-1):
        if ((i>>j)&1):
            res+=tmp%c
            tmp=tmp//c
            c=10
        else:
            c*=10
    ans+=res+tmp
print(ans)