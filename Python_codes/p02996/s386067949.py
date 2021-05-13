n = int(input())
apple = []
for _ in range(n):
    a, b = map(int, input().split())
    apple.append([b, a])
apple = sorted(apple)
count = 0
s = 0
for i in apple:
    if count + i[1] <= i[0]:
        s += 1
        count += i[1]
    else:
        s = 0
        break
print("Yes" if s==n else "No")