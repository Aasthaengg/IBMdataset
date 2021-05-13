n = int(input())
a = list(map(int, input().split()))
ans = 3 ** n
x = 1
for i in range(n):
    if a[i] % 2 == 0:
        x *= 2
print(ans - x)