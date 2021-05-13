n = int(input())
s = [list(input()) for _ in range(n)]

s_dict = dict([])

for i in s:
    key = ''.join(sorted(i))
    try:
        s_dict[key] += 1
    except KeyError:
        s_dict[key] = 1

ans = 0
for v in s_dict.values():
    ans += v * (v - 1) // 2
print(ans)