a, b = map(int, input().split())
t = [0]
for i in range(1, 1000):
    t.append(t[i-1] + i)
print(t[b-a] - b)