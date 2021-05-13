N = int(input())
for i in range(N):
    a, b, c = map(int,input().split())
    if (a**2 + b**2 + c**2 - 2*(max(a,b,c)**2)) == 0:
        print('YES')
    else:
        print('NO')