N,C,K = map(int,input().split())
T = [int(input()) for _ in range(N)]
T.sort()
cnt = 0
pas = 0
time = T[0]
for i in range(N-1):
    pas += 1
    if pas and T[i] - time > K:
        pas,time = 1,T[i]
        cnt += 1
        continue
    if pas == C:
        pas,time = 0,T[i+1]
        cnt += 1
print(cnt+1+(pas and T[N-1]-T[N-2]>=K))