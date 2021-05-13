N = int(input())
A = list(map(int,input().split()))

cnt = 0
ALL = set()
for a in A:
    c = a//400
    if c >= 8:
        cnt+= 1
    else:
        ALL.add(c)

if len(ALL) == 0:
    print(1,cnt)
else:
    print(len(ALL),len(ALL)+cnt)
