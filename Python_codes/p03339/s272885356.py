N = int(input())
S = list(input())
West = [0]*(N+1)
East = [0]*(N+1)
for i in range(N):
    if S[i]=="W":
        West[i+1]=West[i]+1
    else:
        West[i+1]=West[i]
for i in range(N):
    if S[i]=="E":
        East[i+1]=East[i]+1
    else:
        East[i+1]=East[i]
ans = float("inf")
for i in range(N+1):
    tmp = West[i]+(East[N]-East[i])
    if tmp<ans: ans = tmp
print(ans)