l = [0, 0, 0, 0]

for i in range(3):
    a, b = map(int, input().split())
    l[a - 1] += 1
    l[b-1] += 1

for i in l:
    if i == 0 or i >= 3:
        print("NO")
        exit()

print("YES")
