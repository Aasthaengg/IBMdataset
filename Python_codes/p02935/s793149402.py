n = int(input())
v = sorted(list(map(int, input().split())), reverse=True)

while len(v) > 1:
    x = v.pop()
    y = v.pop()
    v.append((x + y) / 2)
    v.sort(reverse=True)

print(*v)