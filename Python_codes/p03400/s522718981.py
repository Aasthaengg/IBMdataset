n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
choco = 0
for i in a:
    default = 1
    num = 0
    while default <= d:
        default += i
        num += 1
    choco += num
print(choco + x)