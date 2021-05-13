n,p = map(int,input().split())
a = list(map(int,input().split()))
flg = True
for i in a:
    if i % 2 != 0:
        flg = False
        break
if flg:
    if p == 0:
        print(2**n)
    else:
        print(0)
else:
    print(2**(n-1))