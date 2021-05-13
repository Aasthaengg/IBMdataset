n = int(input())
a = list(map(int,input().split()))
a.sort()
if n%2 == 0:
    a_l = a[0::2]
    a_r = a[1::2]
    flag = True
    key = 1
    for i,j in zip(a_l,a_r):
        if i!=key or j!=key:
            flag = False
            break
        key += 2
    if flag:
        print(2**(n//2)%(10**9+7))
    else:
        print(0)
else:
    a_l = a[1::2]   #0を一つとばす
    a_r = a[2::2]
    flag = True
    key = 2
    for i,j in zip(a_l,a_r):
        if i!=key or j!=key:
            flag = False
            break
        key += 2
    if flag:
        print(2**(n//2)%(10**9+7))
    else:
        print(0)
