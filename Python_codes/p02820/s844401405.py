n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
history = []
device2point = {'r' : p, 's': r, 'p': s}
device2hand = {'r': 'p', 's': 'r', 'p': 's'}
point = 0
for i in range(n):
    d = t[i]
    if i - k >= 0 and device2hand[d] == history[i-k]:
        history.append(None)
    else:
        point += device2point[d]
        history.append(device2hand[d])
print (point)