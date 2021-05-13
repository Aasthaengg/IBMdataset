N = int(input())
place = {}
for i in range(N):
    place[int(input())] = i

seq = 0
seq_max = 0
prev = 0
for i in range(1, N+1):
    if place[i] >= prev:
        seq += 1
    else:
        seq = 1
    prev = place[i]
    seq_max = max(seq, seq_max)
print(N - seq_max)
