import sys
input = sys.stdin.readline

N,K = list(map(int,input().split()))
count = {}
for i in range(N):
    a,b= list(map(int,input().split()))
    if a in count:
        count[a] += b
    else:
        count[a] = b
ct = sorted(count.items())

for i in range(len(ct)):
    if ct[i][1] >= K:
        print(ct[i][0])
        exit()
    else:
        K -= ct[i][1]

