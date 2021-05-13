n = int(input())
ans = 1
a, b = False, False
x = list(map(int, input().split()))
for i in range(1, n):
    if x[i] > x[i - 1]:
        a = True
    if x[i] < x[i - 1]:
        b = True
    if a and b:
        a, b = False, False
        ans += 1
print(ans)
