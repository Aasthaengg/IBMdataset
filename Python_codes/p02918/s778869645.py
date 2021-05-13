N,K = map(int,input().split())
import sys
S = input()

inside = 0
happy = 0

for i in range(N-1):
    if S[i] == S[i+1]:
        happy += 1
    if S[i] == 'R' and S[i+1] ==  'L':
        inside += 1

happy += 2*(min(K,inside))
if K - inside > 0:
  if S[N-1] == 'R':
    happy += 1
print(happy if happy < N else happy-1)

