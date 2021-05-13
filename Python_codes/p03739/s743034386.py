n = int(input())
a = list(map(int,input().split()))

#マイナススタート
now = 0
count = 0
for i,j in enumerate(a):
    now += j
    if i%2 == 0:
        if now >= 0:
            count += abs(now)+1
            now = -1
    else:
        if now <= 0:
            count += abs(now)+1
            now = 1

#プラススタート
now = 0
count2 = 0
for i,j in enumerate(a):
    now += j
    if i%2 == 0:
        if now <= 0:
            count2 += abs(now)+1
            now = 1
    else:
        if now >= 0:
            count2 += abs(now)+1
            now = -1

print(min(count,count2))