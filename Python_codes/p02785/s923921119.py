import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

n, k = inm()
a = sorted(inl())
print(sum(a[:n-k]) if n > k else 0)