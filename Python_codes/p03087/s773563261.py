N,Q = list(map(int,input().split()))
S = input()
lr = [list(map(int,input().split())) for i in range(Q)]

count = 0
countList = [0 for i in range(N)]
for i in range(1, N):
    if S[i - 1] == 'A' and S[i] == 'C':
        count += 1
    countList[i] = count

for i in range(Q):
    l = lr[i][0]
    r = lr[i][1]
    lCount = countList[l - 1]
    rCount = countList[r - 1]
    print(rCount - lCount)