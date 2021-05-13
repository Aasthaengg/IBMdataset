import collections
N = int(input())
a = [0] * N
for i in range(N):
    a[i] = int(input())
def solve():
    return any(x % 2 == 1 for x in a)
print('first' if solve() else 'second')
