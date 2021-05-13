n, k = map(int, input().split())
s = list(str(input()))
unhappy = 0
for i in range(n - 1):
    if s[i] != s[i + 1]:
        unhappy += 1
print(n - unhappy - 1 + min(2 * k, unhappy))