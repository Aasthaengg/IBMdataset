import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m, q = map(int, input().split())
abcd = [0] * q
for i in range(q):
    abcd[i] = list(map(int, input().split()))

def dfs(seq):
    if len(seq) == n:
        yield seq
    else:
        if seq:
            last = seq[-1]
        else:
            last = 1
        for i in range(last, m+1):
            new_seq = seq.copy()
            new_seq.append(i)
            yield from dfs(new_seq)

seq = dfs([])
ans = 0
for s in seq:
    tmp_ans = 0
    for a, b, c, d in abcd:
        if s[b-1] - s[a-1] == c:
            tmp_ans += d
    ans = max(ans, tmp_ans)
print(ans)
