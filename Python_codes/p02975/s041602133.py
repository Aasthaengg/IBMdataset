import sys,collections
input = sys.stdin.readline

N = int(input())
a =list(map(int,input().split()))

if sum(a) == 0:
    print('Yes')
    exit()

if N%3 != 0:
    print('No')
    exit()    

ac = collections.Counter(a)

if len(ac) == 2 and ac[0] ==N/3:
    print('Yes')
    exit()


if len(ac) != 3 :
    print('No')
    exit()
else:
    lk1,lk2,lk3 = ac.keys()
    lv1,lv2,lv3 = ac.values()
if lv1 == lv2 ==lv3:
    if lk1^lk2 == lk3:
        print('Yes')
    else:
        print('No')
else:
    print('No')
    exit()