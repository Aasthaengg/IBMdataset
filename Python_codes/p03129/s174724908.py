N,K = map(int,input().split())

if N % 2 == 0:
    temp = N / 2
else:
    temp = N / 2 + 1

ans = 'YES'

if K > temp:
    ans = 'NO'
    
print(ans)
