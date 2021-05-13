import sys, itertools

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))

S = list(itertools.accumulate(A))

mini = 10 ** 18
for i in range(N):
    mini = min(mini, abs(S[N - 1] - 2 * S[i]))

print(mini)
