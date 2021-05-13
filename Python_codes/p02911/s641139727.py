N, K, Q = map(int, input().split())
A = tuple([int(input()) for q in range(Q)])
# N人参加、初期状態で全員がKポイント
# 誰かが正解すると、それ以外の全員が1ポイント下がる
# i番目に正解したのはAi
counts = [0 for i in range(N)]
for a in A:
  counts[a-1] += 1

for i in range(N):
  print('Yes' if (K - (Q - counts[i])) >= 1 else 'No')