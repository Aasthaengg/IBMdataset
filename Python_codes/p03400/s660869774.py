n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

eat = 0
for i in range(len(a)):
    for j in range(1, d+1, a[i]):
        eat += 1

print(x + eat)


