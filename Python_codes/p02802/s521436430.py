N,M=map(int,input().split())
correct=[]
penalty=[0 for i in range(N+1)]
for i in range(M):
  p,S=input().split()
  p=int(p)
  if S=="AC":correct.append(p)
  else:
    if p not in correct: penalty[p] += 1

correct = set(correct)

ans = 0
for p in correct:
  ans += penalty[p]
      
print(' '.join([str(len(correct)), str(ans)]))