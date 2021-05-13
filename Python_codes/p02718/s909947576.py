N, M = map(int, input().split())
vote = list(map(int, input().split()))
count = 0
for i in range(N):
    if vote[i] < sum(vote)*1/(4*M):
        pass
    else:
        count+=1
if count >= M:
    print('Yes')
else:
    print('No')

