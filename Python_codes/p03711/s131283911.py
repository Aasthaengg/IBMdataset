x, y = map(int, input().split())
t = [0]*13
t[4] = t[6] = t[9] = t[11] = 1
t[2] = 2
print('Yes' if t[x] == t[y] else 'No')