
A, B, C, K = map(int, input().split())
r = K % 2
if r == 0:
    ans = A - B
else:
    ans = B - A

if abs(ans) > 10**18:
    print('Unfair')
else:
    print(ans)