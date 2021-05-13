n = int(input())
a_li = list(map(int,input().split()))
b_li = list(map(int,input().split()))

kaisu = 0
ukeire = 0
for a,b in zip(a_li,b_li):
    if a>b:
        kaisu += a-b
    elif a<b:
        ukeire += (b-a)//2
if ukeire >= kaisu:
    print('Yes')
else:
    print('No')