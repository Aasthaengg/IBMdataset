import sys
readline = sys.stdin.buffer.readline

N = int(readline())
B = list(map(int, readline().split()))

B.append(float('inf'))

mins = [B[0]]

for i in range(1, N):
    mins.append(min(B[i-1], B[i]))

print(sum(mins))