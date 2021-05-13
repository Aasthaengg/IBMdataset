s = input().split()

n = int(s[0])
k = int(s[1])

snakes = []

p = input().split()
for i in range(n):
    q = int(p[i])
    snakes.append(q)

snakes.sort()

answer = 0

for i in range(k):
    x = snakes.pop()
    answer += x

print(answer)