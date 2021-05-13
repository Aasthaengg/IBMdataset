s = input()
n = int(s)

house = []

p = input().split()
for i in range(n):
    q = int(p[i])
    house.append(q)

house.sort()

answer = house[n - 1] - house[0]

print(answer)