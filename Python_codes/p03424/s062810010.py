N = int(input())
S = list(input().split())
ans = len(set(S))
if ans <=3:
    print('Three')
else:
    print('Four')
