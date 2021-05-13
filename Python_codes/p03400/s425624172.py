n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
total = x
for i in a:
    chocos = (d - 1) // i
    total += chocos + 1
print(total)