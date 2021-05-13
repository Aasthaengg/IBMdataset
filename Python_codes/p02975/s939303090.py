from collections import Counter
n = int(input())
a = [int(i) for i in input().split()]
a_set = set(a)

if len(a_set)==1:
    if sum(a_set)==0:
        print('Yes')
    else:
        print('No')
elif len(a_set)==2:
    a_1,a_2 = sorted(a_set)
    if a_1==0:
        if a.count(a_1)*3==n:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
elif len(a_set)==3:
    a_1,a_2,a_3= a_set
    if a.count(a_1)==a.count(a_2) and a.count(a_2)==a.count(a_3):
        if a_1^a_2==a_3:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')    