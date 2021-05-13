def dfs(n):
    if n == 0:return 0
    return dfs(n % format(n, "b").count("1")) + 1
n = int(input())
x = input()
c = x.count("1")
a = int(x, 2)
if c == 1:
    for i in range(n):
        if x[i] == "1":
            print(0)
        elif i == n - 1:
            print(2)
        else:
            print(1)
else:
    j, k = a % (c + 1), a % (c - 1)
    for i in range(n):
        if x[i] == "1":print(dfs((k - pow(2, n - i - 1, c - 1)) % (c - 1)) + 1)
        else:print(dfs((j + pow(2, n - i - 1, c + 1)) % (c + 1)) + 1)