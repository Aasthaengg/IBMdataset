N = int(input())
S = input()

white_count = [0]*(N+1)
black_count = [0]*(N+1)

for i in range(N):
  black_count[i+1] = black_count[i]
  if S[i] == "#":
    black_count[i+1] += 1
  
S = S[::-1]
for i in range(N):
  white_count[i+1] = white_count[i]
  if S[i] == ".":
    white_count[i+1] += 1

    
answer = 10**6
for i in range(N+1):
  answer = min(answer,black_count[i]+white_count[N-i])
  
print(answer)