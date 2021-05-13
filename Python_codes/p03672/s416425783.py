S = input()

start = 2
if len(S) % 2:
    start = 1

for i in range(start,len(S),2):
    t = S[:-i]
    n = len(t) // 2
    if t[:n] == t[n:]:
        print(len(t))
        break