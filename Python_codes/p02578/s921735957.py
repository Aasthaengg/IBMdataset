n = int(input())
a_list = [int(x) for x in input().split()]
ans = h = 0
for a in a_list:
    if a > h:
        h = a
    else:
        ans += h - a
print(ans)