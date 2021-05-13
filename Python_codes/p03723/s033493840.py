a, b, c = map(int, input().split())
count = 0
for i in range(10**3):
    if a%2 != 0 or b%2 != 0 or c%2 != 0:
        print(count)
        exit()
    a, b, c = b/2 + c/2, a/2 + c/2, a/2 + b/2
    count += 1
print(-1)