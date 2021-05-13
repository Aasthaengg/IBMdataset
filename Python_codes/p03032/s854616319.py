import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,K,*V = map(int,read().split())

vals = []
for L in range(N+1):
    for R in range(N+1):
        if L+R > N:
            break
        get = V[:L] + V[N-R:]
        rest = K - (L+R)
        if rest < 0:
            break
        get.sort(reverse=True)
        for _ in range(min(len(get),rest)):
            if get[-1] < 0:
                get.pop()
            else:
                break
        vals.append(sum(get))

answer = max(vals)
print(answer)
