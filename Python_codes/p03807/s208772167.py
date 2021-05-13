n  = int(input())
l = [int(i) for i in input().split()]

odd = [i for i in l if i % 2]

if len(odd) % 2:
    print('NO')
else:
    print('YES')