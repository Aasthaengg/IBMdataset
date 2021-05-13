#ABC058 A - ι⊥l
si = lambda: input()
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
a,b,c = map(int, input().split())
if b-a == c-b:
    print('YES')
else:
    print('NO')