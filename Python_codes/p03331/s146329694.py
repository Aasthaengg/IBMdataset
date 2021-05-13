n = int(input())
ans = []
for i in range(1, n):
    a = sum(map(int, str(i)))
    b = sum(map(int, str(n - i)))
    ans.append(a + b)
print(min(ans))