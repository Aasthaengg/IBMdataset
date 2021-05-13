n = int(input())
li = list(map(int, input().split()))
od = [x for x in li if x%2==1]

if len(od)%2==0:
    print('YES')
else:
    print('NO')