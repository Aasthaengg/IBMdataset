n = int(input())
apple = []
for _ in range(n):
    apple.append(int(input()))
apple = sorted(apple)
apple.append(0)
count = 0
ans = 1
for i in range(n):
    if apple[i] == apple[i + 1]:
        ans += 1
    else:
        if ans%2 == 0:
            ans = 1
        else:
            count += 1
print(count)
