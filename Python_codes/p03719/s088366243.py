# ABC061 A - Between Two Integers
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a,b,c = nm()

if a<=c<=b:
    print('Yes')
else:
    print('No')