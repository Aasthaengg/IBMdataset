s = input().split('T')
dx = list(map(len, s[0::2]))
dy = list(map(len, s[1::2]))
x, y = map(int, input().split())

def check(start, ds, goal):
    cands = {start}
    for d in ds:
        new_cands = set()
        for c in cands:
            new_cands.add(c - d)
            new_cands.add(c + d)
        cands = new_cands
    return goal in cands

x_ok = check(dx[0], dx[1:], x)
y_ok = check(0, dy, y)

print('Yes' if x_ok and y_ok else 'No')
