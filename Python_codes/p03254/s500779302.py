# -*- coding:utf-8 -*-
N,x = map(int,input().split())
a = list(map(int,input().split()))

cnt = 0
a.sort()

while x > 0:
    if cnt >= N:
        if x > 0:
            cnt -= 1
            break
        else:
            break
    elif a[0] > x:
        break
    else:
        tmp = a.pop(0)
        x -= tmp
        cnt+=1


print(cnt)
