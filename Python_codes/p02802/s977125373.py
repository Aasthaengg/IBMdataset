N,M = map(int,input().split())
correct = [0]*N
penalty = [0]*N
ans_c,ans_p = 0,0
for i in range(M):
    p,s = input().split()
    p = int(p)
    if s=="AC":
        if correct[p-1]==0:
            correct[p-1]+=1
    if s=="WA":
        if correct[p-1]==0:
            penalty[p-1]+=1

ans_penalty = 0
for i in range(N):
    if correct[i]>=1:
        ans_penalty+=penalty[i]
print(sum(correct),ans_penalty)