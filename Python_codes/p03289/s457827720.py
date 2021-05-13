import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

S = input()

if S[0] == "A" and S[2:-1].count("C") == 1 and S.count("A") == 1 and S.count("C") == 1:
    S = S.replace("A", "")
    S = S.replace("C", "")
    if S == S.lower():
        print('AC')
        quit()
print('WA')
