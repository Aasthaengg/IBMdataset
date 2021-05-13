a = list(map(int,input().split()))
M = max(a)
if (3 * M - sum(a))%2 == 0:
    print((3 * M - sum(a))//2)
else:
    print((3 * (M+1) - sum(a))//2)