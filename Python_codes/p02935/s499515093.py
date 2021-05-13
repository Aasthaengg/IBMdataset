n = int(input())
v_li = [int(w) for w in input().split()]

v_li.sort()

ans = v_li[0]
for i in v_li[1:]:
    ans = (ans + i) / 2
print(ans)
