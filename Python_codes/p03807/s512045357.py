N = int(input())
A = list(map(int,input().split()))
AA = sum([i%2 for i in A])
if N == 1:
    print('YES')
    exit()
if AA % 2 == 1:
    print('NO')
    exit()
print('YES') 
