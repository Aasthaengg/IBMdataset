import sys
input = sys.stdin.readline

n, k, q = [int(w) for w in input().split()]


score = [0] * n

for i in range(q):
    a = int(input())
    score[a - 1] += 1


for s in score:
    print('Yes' if s + k - q > 0 else 'No')
