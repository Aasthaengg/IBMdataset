n,k,s = map(int,input().split())
if s < 10 ** 9:
    ans = list([str(s)]*k + [str(s+1)]*(n-k))
else:
    ans = list([str(s)]*k + ['1']*(n-k))
print(' '.join(ans))