N,K,Q = map(int,input().split())
A = [int(input()) for _ in range(Q)]
score_board = [K-Q for _ in range(N)]

for a in A:
  score_board[a-1] += 1
  
for res in score_board:
  if res > 0:
    print("Yes")
  else:
    print("No")