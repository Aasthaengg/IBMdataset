import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = readline().decode().rstrip()

ans = 'WA'
if S[0] == 'A':
    if S[2:-1:].count('C') == 1:
        ans = 'AC' if S[1::].replace('C', "").islower() else 'WA'
print(ans)
