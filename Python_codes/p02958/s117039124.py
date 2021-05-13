N = int(input())
Sort = [str(x) for x in range(1,N+1)]
P = [str(x) for x in input().split()]

Count = 0
for T in range(0,N):
    if Sort[T] != P[T]:
        Count += 1
if Count==0 or Count==2:
    print('YES')
else:
    print('NO')