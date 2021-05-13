n = int(input())
l = []
for i in range(n):
    i = list(map(int,input().split()))
    l.append(i)
tmp = 0

for j in reversed(range(n)):
    l[j][0] += tmp
    if l[j][0]%l[j][1] != 0:
        tmp += l[j][1] - l[j][0]%l[j][1]

print(tmp)