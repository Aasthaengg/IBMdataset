a, b = map(int, input().split())
c = b - a
t = [1]
for i in range(1100):
    t.append(t[i]+i+2)
idx = 0
for i in range(1000):
    if t[i+1] - t[i] == c:
        idx = i + 1
        break

print(idx * (idx+1)//2-a)