n=int(input())
a=[int(i) for i in input().split()]
if(len(set(a))==n):
    print('YES')
else:
    print('NO')