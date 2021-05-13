n = int(input())
li = list(map(int,input().split()))
se = set(li)
if len(se) == 1:
    if sum(se) == 0:
        print('Yes')
    else:
        print('No')
elif len(se) == 2:
    a,b = sorted(se)
    if a == 0:
        if li.count(a) * 3 == n:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
elif len(se) == 3:
    a,b,c = se
    if li.count(a) == li.count(b) == li.count(c):
        if a^b == c:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')
