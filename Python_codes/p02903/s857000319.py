import sys

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split())) # 
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

H, W, A, B = rl()
answer = ['0'*(W-A) + '1'*A for _ in range(H-B)]
answer += ['1'*(W-A) + '0'*A for _ in range(B)]
for x in answer:
    print(*x, sep='')
