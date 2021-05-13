N = int(input())
S = list(input())

row = [0]*(N+2)
for i in range(N):
    if S[i] =='E':
        row[i+1] = row[i] + 1
    else:
        row[i+1] = row[i]
answer = [0]*N
for i in range(N):
    answer[i] += (i - row[i])
    a = row [N] - row[i+1]
    answer[i] += a
#print(S)
#print(row)
#print(answer)
print(min(answer))
