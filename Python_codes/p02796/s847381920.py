N = int(input())
pos_list = []
for _ in range(N):
    X, L = map(int, input().split())
    pos_list.append([X + L, X - L])
sorted_data = sorted(pos_list)
# print(pos_list)
ans = 0
current = -(10 ** 9)
for val in sorted_data:
    if current <= val[1]:
        ans += 1
        current = val[0]
print(ans)
