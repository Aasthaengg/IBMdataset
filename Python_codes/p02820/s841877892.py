n, K = map(int, input().split())
R, S, P = map(int, input().split())
t = input()

hands = ["any"]*n

for i in range(n):
  if i-K < 0 or hands[i-K] != t[i]:
    hands[i] = t[i]
    
score = 0
for h in hands:
  if h == "r":
    score += P
  elif h == "s":
    score += R
  elif h == "p":
    score += S
print(score)