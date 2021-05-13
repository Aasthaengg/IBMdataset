n = int(input())
k = int(input())

l = [1]
for _ in range(n):
    l.append(min(l[-1] * 2, l[-1] + k))

print(l[-1])