a_list = list(map(int, input().split()))

ans = 0

a0 = min(a_list)
a_list.remove(a0)
a1 = min(a_list)
a_list.remove(a1)
ans += abs(a1 - a0)
a2 = min(a_list)
ans += abs(a2 - a1)

print(ans)
