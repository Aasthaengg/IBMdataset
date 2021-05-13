# 
si = lambda: input()
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
a=ni()
b=ni()

if a>b:
    print('GREATER')
elif a==b:
    print('EQUAL')
elif a<b:
    print('LESS')