from collections import Counter

n = int(input())
l1 = list(map(int,input().split()))
l1_cnt = Counter(l1) 

m = int(input())
l2 = list(map(int,input().split()))
l2_cnt = Counter(l2) 
l2_set=set(l2)

for i in l2_set:
    if l2_cnt[i]<=l1_cnt[i]:
        continue
    else:
        print('NO')
        break
else:
    print('YES')

