
(n, k) = map(int, input().split())
(a, b) = zip(*[map(int, input().split()) for _ in range(n)])

cnt_dict = {}
for i in range(n):
    if a[i] not in cnt_dict.keys():
        cnt_dict[a[i]] = 0
    cnt_dict[a[i]] += b[i]

length = 0
for a_i in sorted(cnt_dict.keys()):
    length += cnt_dict[a_i]
    if length >= k:
        ans = a_i
        break

print(ans)
