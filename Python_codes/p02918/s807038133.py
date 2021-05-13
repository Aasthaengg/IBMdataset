n, k = map(int, input().split())
s = "X" + input() + "X"
t = [s[i] == s[i + [1, -1][s[i] == "L"]] for i in range(1, n + 1)]
print(min(sum(t) + k * 2, n - 1))