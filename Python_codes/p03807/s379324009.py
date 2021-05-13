N = int(input())
li = list(map(int,input().split(' ')))

li_pm = [0 if i%2==0 else 1 for i in li]

if (li_pm.count(1))%2 == 0:print('YES')
else:print('NO')