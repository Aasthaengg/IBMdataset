N,M =map(int,input().split())
a = list(map(int,input().split()))
total_vote = sum(a)
a.sort(reverse=True)
if a[M-1] >= total_vote / (4*M):
    print('Yes')
else:
    print('No')