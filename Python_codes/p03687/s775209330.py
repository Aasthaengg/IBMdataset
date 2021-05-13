string = input()
start = len(string)
targets = set(string)
ans = float('inf')
for a in targets:
    prev = string
    while not all(c == a for c in prev):
        new = ''
        for idx in range(len(prev) - 1):
            if a in (prev[idx], prev[idx+1]):
                new += a
            else:
                new += prev[idx]
        prev = new
    score = start - len(prev)
    ans = min(ans, score)

print(ans)