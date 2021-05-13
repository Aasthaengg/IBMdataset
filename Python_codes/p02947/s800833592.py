N = int(input())
S = [0]*N
for i in range(N):
    S[i] = ''.join(sorted(str(input())))
answer = 0
numdic = {}
for i in range(N):
    if S[i] in numdic:
        answer += numdic[S[i]]
        numdic[S[i]] +=1
        
    else:
        numdic[S[i]] = 1
    
print(answer)