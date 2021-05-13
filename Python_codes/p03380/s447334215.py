n = int(input())
a = list(map(int, input().split()))
m = max(a)
a = sorted(a)
ans = 0
for i in a:
    if abs(m/2-i) < abs(m/2-ans):
        ans = i
print(m, ans)