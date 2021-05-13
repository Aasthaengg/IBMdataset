N = int(input())
a = sorted(list(map(int, input().split())))
nyu = []
ma = a[-1]
mi = a[0]
i=0
while i!=N-2:
    if a[i+1]>=0:
        nyu.append([mi, a[i+1]])
        mi -= a[i+1]
    else:
        nyu.append([ma, a[i+1]])
        ma -= a[i+1]
    i += 1
nyu.append([ma, mi])
print(nyu[N-2][0]-nyu[N-2][1])
for i in range(N-1):
    print(nyu[i][0], nyu[i][1])