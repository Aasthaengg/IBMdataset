import collections
N = int(input())
S = list(input())
cnt = 0

ans = [0]*N

for i in range(1,N):
    if S[i] == "E":
        cnt += 1
ans[0] = cnt

for i in range(1,N):
    if S[i-1] == 'E' and S[i] == 'E':
        ans[i] = ans[i-1]-1
    elif S[i-1] == "W" and S[i] == 'W':
        ans[i] = ans[i-1]+1
    else:
        ans[i] = ans[i-1]
     
print(min(ans))
