n = int(input())
a = [int(x) for x in input().split()]
ans = 0
for i, a_i in enumerate(a):
    if a[a_i - 1] == i + 1: ans += 1
print(int(ans/2))