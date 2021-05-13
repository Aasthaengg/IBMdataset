import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

S = input()

last = ""
tmp = ""
ans = 0
for s in S:
    tmp += s
    if tmp == last:
        continue
    # print(tmp)
    last = tmp
    tmp = ""
    ans += 1
print(ans)