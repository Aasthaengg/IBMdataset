N,C,K = map(int,input().split())
T = [int(input()) for _ in range(N)]
T.sort()
bus = 0
count = 0
j = 0
for i in range(N-1):
  count += 1
  if count >= C or T[i+1] > T[j]+K:
    bus += 1
    j += count
    count = 0
  if i == N-2:
    count += 1
    if count%C == 0:
      bus += count//C
    else:
      bus += count//C+1
print(bus)