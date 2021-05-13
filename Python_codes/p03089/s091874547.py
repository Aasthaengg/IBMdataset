#!/usr/bin/env python3
n, *b = map(int, open(0).read().split())
ans = []
for i in reversed(range(n)):
    for j in reversed(range(i + 1)):
        if b[j] == j + 1:
            ans.append(b.pop(j))
            break
    else:
        print(-1)
        exit()
print(*reversed(ans), sep="\n")
