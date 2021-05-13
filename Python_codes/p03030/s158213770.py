# 128 B

n = int(input())
s = []

for i in range(n):
    tp = list(input().split())
    s.append(tp)

for i in range(n):
    s[i][1] = int(s[i][1]) * (-1)
    s[i].append(i+1)
s.sort()

for i in range(n):
    print(s[i][2])

