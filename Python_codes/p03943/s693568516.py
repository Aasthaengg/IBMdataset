import itertools
a,b,c = map(int,input().split())

ans = [a,b,c]
sum_1 = 0
sum_2 = 0
for i in range(3):
    if i == ans.index(max(ans)):
        sum_1 += ans[i]
    else:
        sum_2 += ans[i]

if sum_1 == sum_2:
    print('Yes')
else:
    print('No')