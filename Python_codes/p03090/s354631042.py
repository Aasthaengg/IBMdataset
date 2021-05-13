import sys

stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))  # applies to only numbers
rs = lambda: stdin.readline().rstrip()  # ignores trailing space

N = ri()
answer_list = []
pair = N if N&1 else N+1
for i in range(1, N):
    for j in range(i+1, N+1):
        if i+j == pair:
            continue
        else:
            answer_list.append((i, j))

print(len(answer_list))
for x in answer_list:
    print(*x)
