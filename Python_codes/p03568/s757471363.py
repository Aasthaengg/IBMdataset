n = int(input())
a = list(map(int, input().split()))
num = 1
for i in a:
    if i % 2 == 0:
        num *= 2
    else:
        num *= 1
ans = 1
for i in range(n):
    ans *= 3
print(ans - num)