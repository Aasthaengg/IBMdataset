S = list(input())
N = len(S)
for i in range(N):
    if S[i] == 'A':
        start = i
        break
for i in range(N-1,0,-1):
    if S[i] == 'Z':
        end = i
        break

print(end-start+1)