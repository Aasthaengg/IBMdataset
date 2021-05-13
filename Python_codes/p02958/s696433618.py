import sys
N = int(input())
array = list(map(int,input().split()))
array_base = [ I for I in range(1,N+1) ]

dic = {}
for I in range(N):
    if array[I] != I + 1:
        dic[I] = array[I]

if not (len(dic) == 2 or len(dic) == 0):
    print('NO')
else:
    print('YES')