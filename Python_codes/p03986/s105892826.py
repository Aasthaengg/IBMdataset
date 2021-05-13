from collections import deque
X = input()

scan = deque()

for c in X:
    # print(scan)
    if c == 'S':
        scan.append(c)
    else:
        if not scan or scan[-1] == 'T':
            scan.append('T')
        else:
            scan.pop()
print(len(scan))
