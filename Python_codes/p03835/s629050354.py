import sys

num = sys.stdin.readline().split(' ')
K = int(num[0])
S = int(num[1])

counter = 0
for i in range(K+1):
    for j in range(K+1):
        if 0 <= S-i-j <= K:
            counter += 1
        else:
            continue

print(counter)