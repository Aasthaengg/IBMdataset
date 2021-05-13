s = input()
n = int(s)

v = input()
k = int(v)

locations = []

sub = []

answer = 0

x = input().split()
for i in range(n):
    y = int(x[i])
    locations.append(y)

for i in range(len(locations)):
    sub.append(min(locations[i], k - locations[i]) * 2)

for i in range(len(sub)):
    answer += sub[i]

print(answer)