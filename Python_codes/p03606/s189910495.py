num = 0
for _ in range(int(input())):
    l, r = map(int, input().split())
    num += r - l + 1
print(num)