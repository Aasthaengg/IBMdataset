n =input()
m = list(map(int,input().split()))
if len(m) == len(list(set(m))):
    print('YES')
else:
    print('NO')