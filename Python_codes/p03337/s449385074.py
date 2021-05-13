
l = list(map(int, input().split()))

s = []
s.append(l[0] + l[1])
s.append(l[0] - l[1])
s.append(l[0] * l[1])

print(max(s))