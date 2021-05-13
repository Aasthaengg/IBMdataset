n,k = map(int,input().split())
if k % 2 == 1:
    print((n//k)**3)
else:
    cnt1 = n//k
    cnt2 = n//(k//2)
    print(cnt1**3+(cnt2-cnt1)**3)