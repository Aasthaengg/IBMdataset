n=int(input())

a=[int(input()) for _ in range(n)]

flag=0
for aa in a:
    if aa%2==1:
        flag=1

if flag==0:
    print("second")
else:
    print("first")

###1個
#111
#奇数ならfirst 偶数ならsecond

###２個
#111
#111
#奇数奇数ならfirst
#11
#11
#偶数偶数ならsecond
#

