n = int(input())
a = [int(input()) for _ in range(n)]
ans = [x for x in a if x%2 != 0]

if len(ans) == 0:
    print('second')
else:
    print('first')
