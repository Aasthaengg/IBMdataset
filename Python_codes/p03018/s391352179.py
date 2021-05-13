import sys
stdin = sys.stdin
 
ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

S = rs()
S = S.replace('BC', 'D')
cnt_A = 0
answer = 0
for s in S:
    if s == 'A':
        cnt_A += 1
    elif s == 'D':
        answer += cnt_A
    else:
        cnt_A = 0
print(answer)