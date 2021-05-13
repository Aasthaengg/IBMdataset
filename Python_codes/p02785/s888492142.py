N, K = map(int, input().split())
H = list(map(int, input().split()))
H = sorted(H)
SUM = 0

if K >= N:
    print(0)
    exit()


    
for i in range(len(H)-K):
    SUM = SUM + H[i]


print(SUM)