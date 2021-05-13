N = int(input())
d = []
for i in range(N):
    d.append(int(input()))

d = set(sorted(d))

print(len(d))