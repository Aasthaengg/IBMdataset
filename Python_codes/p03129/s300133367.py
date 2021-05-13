n,k = map(int,input().split())

if n%2==0: mx=n//2
else: mx=n//2+1

if mx>=k: print('YES')
else: print('NO')