import sys
import fractions

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
NS = list(str(N))

q, mod = divmod(N, 10)
i = -1
while q:
    if mod < 8:
        NS[i:] = ['9' for i in range(-i)]
        NS[i-1] = str(int(NS[i-1]) - 1)
    i -= 1
    q, mod = divmod(q, 10)

print(sum(map(int, NS)))
