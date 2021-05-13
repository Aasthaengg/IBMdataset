n = int(input())
a = list(map(int,input().split()))
ki = [i for i in a if i%2!=0]
if len(ki)%2 != 0:
    print('NO')
else:
    print('YES')