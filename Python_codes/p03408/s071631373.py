N = int(input())
blues=[]
for i in range(N):
  blues.append(input())
M = int(input())
reds=[]
for i in range(M):
  reds.append(input())

ma = 0

blueset = set(blues)

for S in blueset:
  ma = max(ma,blues.count(S)-reds.count(S))
print(ma)