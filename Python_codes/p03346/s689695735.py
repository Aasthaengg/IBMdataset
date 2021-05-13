
N = int(input())

P = [int(input()) for _ in range(N)]

idxs = [0] * N
for i in range(N):
    idxs[P[i]-1] = i



max_cnt = 0
curr = 0
for i in range(N):
    if i == 0:
        max_cnt = 1
        curr = 1
    else:
        
        if idxs[i] > idxs[i-1]:
            curr += 1
            max_cnt = max(max_cnt, curr)
        else:
            curr = 1
    

print(N - max_cnt)
