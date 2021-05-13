N = int(input())
S = input()

cumdots = [0] * (N+1)

for i in range(N):
  cumdots[i+1] = cumdots[i] + (1 if S[i]=="." else 0)
  
#print(cumdots)

hands = N+1
for i in range(N):
  #i番目までをdot, i+1番目からsharpとする
  leftops = i - cumdots[i]
  rightops = cumdots[N] - cumdots[i+1]
  hands = min(hands, leftops + rightops)
  
print(hands)