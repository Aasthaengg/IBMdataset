from sys import argv

debug = "a" in argv
n = int(input())
a = tuple(map(int, input().split()))
ans = 0
for x in range(n - 2):
    if debug:
        print(x, a[x], a[x + 1], a[x + 2])
    if sorted([a[x], a[x + 1], a[x + 2]])[1] == a[x + 1]:
        ans += 1
print(ans)