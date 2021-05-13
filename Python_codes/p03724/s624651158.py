N, M = map(int,input().split())
freq = [True]*N
for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    if freq[a]:
        freq[a] = False
    else:
        freq[a] = True

    if freq[b]:
        freq[b] = False
    else:
        freq[b] = True

ans = all(freq)
if ans:
    print('YES')
else:
    print('NO')
