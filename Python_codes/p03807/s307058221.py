n = int(input())
a = list(map(int,input().split()))
odd = len([i for i in a if i%2==1])
if odd%2 != 0:
    print('NO')
else:
    print('YES')
