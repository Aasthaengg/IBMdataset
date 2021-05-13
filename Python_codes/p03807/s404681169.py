n = int(input())
A = [int(a) for a in input().split()]

cnt =0
for i in range(0, n):
    if A[i]%2 != 0:
        cnt+=1

if cnt%2!=0:
    print('NO')

else:
    print('YES')            
