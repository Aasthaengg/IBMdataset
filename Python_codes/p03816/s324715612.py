from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

l = 0
r = N-1
count = 0

M = defaultdict(int)
for a in A:
    if M[a] > 0:
        count += 1
    M[a] += 1

if count % 2 == 0:
    print(N-count)
else:
    print(N-(count+1))
