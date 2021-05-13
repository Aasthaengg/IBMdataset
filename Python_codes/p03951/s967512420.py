N = int(input())
S = input()
T = input()
answer = 2*N
for i in range(N):
  if S[N-i-1:] == T[:i+1]:
    answer = 2*N-i-1
print(answer)