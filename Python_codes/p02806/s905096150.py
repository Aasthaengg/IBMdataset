from sys import stdin
N = int(stdin.readline().rstrip())
ST = []
for i in range(N):
    s, t = stdin.readline().rstrip().split()
    ST.append((s, int(t)))
X = stdin.readline().rstrip()
for i in range(N):
    if ST[i][0] == X:
        print(sum(st[1] for st in ST[i+1:]))