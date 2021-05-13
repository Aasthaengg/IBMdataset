from collections import defaultdict, deque, Counter
def inpl(): return list(map(int, input().split()))

N, K = inpl()
print(N-K+1)