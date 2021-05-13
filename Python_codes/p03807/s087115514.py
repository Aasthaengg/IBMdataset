n = int(input())
A = list(map(int,input().split()))
A_g = [i for i in A if i % 2 == 0]
A_k = [i for i in A if i % 2 == 1]

if len(A_k) % 2 == 1:
    print('NO')
else:
    print('YES')