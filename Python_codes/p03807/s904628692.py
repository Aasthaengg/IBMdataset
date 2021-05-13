n = int(input())
a = list(map(int,input().split()))

n_odd = sum([ai%2 for ai in a])
if(n_odd % 2==0):
    print('YES')
else:
    print('NO')