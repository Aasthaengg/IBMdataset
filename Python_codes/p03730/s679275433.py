A,B,C = list(map(int,input().split()))
lis = [ (A * i) % B for i in range(1,B+1)]
if C in lis:
    print('YES')
else:
    print('NO')
