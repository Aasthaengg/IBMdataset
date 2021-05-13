N,L = map(int,input().split())
c = 0
if L >= 0:
    skip = 0
else:
    if N - (-L) > 0:
        skip = L*-1
    else:
        skip = N-1
for i in range(N):
    if i == skip:
        continue
    c += L+i
print(c)