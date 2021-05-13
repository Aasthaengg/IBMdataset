def linear_search(s, n, key):
    for i in s:
        if i == key:
            return 1
    return 0

n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))
ans = 0
for i in t:
    if linear_search(s, n, i) != 0:
        ans += 1
print(ans)
