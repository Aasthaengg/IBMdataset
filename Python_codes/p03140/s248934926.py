def solve(n, a, b, c):
    ans = 0
    for i in range(n):
        ans += len(set([a[i], b[i], c[i]])) - 1
    return ans

n = int(input())
a = input()
b = input()
c = input()
print(solve(n, a, b, c))