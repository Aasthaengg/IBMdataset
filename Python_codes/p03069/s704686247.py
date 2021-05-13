N = int(input())
S = input()

ws = [0]
for c in S:
    ws.append(ws[-1] + int(c=='.'))

ans = N
for i,w in enumerate(ws):
    rw = ws[-1] - w
    lb = i - w
    ans = min(ans, rw+lb)
print(ans)