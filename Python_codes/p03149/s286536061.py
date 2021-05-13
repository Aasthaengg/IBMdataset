# A 
si = lambda: input()
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
a=nl()

if 1 in a and 9 in a and 7 in a and 4 in a:
    print('YES')
else:
    print('NO')

