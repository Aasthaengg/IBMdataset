import sys
stdin = sys.stdin
 
ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

S = list(rs())
cur = 'D'
answer = 0
A_cnt = 0
for s in S:
    if cur == 'A':
        if s == 'A':
            A_cnt += 1
        elif s == 'B':
            cur = s
        else:
            cur = 'D'
            A_cnt = 0
    elif cur == 'B':
        if s == 'A':
            A_cnt = 1
            cur = s
        elif s == 'B':
            A_cnt = 0
            cur = 'D'
        elif s == 'C':
            answer += A_cnt
            cur = s
        else:
            cur = 'D'
            A_cnt = 0
    elif cur == 'C':
        if s == 'A':
            A_cnt += 1
            cur = s
        elif s == 'B':
            cur = s
        else:
            cur = 'D'
            A_cnt = 0
    else:
        if s == 'A':
            A_cnt += 1
            cur = s
        else:
            A_cnt = 0
            cur = 'D'

print(answer)
