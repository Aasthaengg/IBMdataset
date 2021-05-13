n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
list = [0]
x, y = 0, 0

for i in range(len(v)):
    if v[i] > c[i]:
        x += int(v[i])
        y += int(c[i])
        list.append(x - y)
    else:
        continue

print(max(list))