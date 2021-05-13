# B 
si = lambda: input()
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
n=ni()
a=nl()
a=[x%2 for x in a]
if sum(a)%2==0:
    print('YES')
else:
    print('NO')
