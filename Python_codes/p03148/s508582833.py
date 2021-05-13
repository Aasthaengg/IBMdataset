import sys
input = sys.stdin.readline
N, K = map(int, input().split())

sushi_array = []

sushi_count = [-1] * N
sushi_kind = 0
for i in range(N):
    t, d = map(int, input().split())
    sushi_array.append([t - 1, d])
    if sushi_count[t - 1] == -1:
        sushi_count[t - 1] = 0
        sushi_kind += 1

sushi_array = sorted(sushi_array, key=lambda x: -x[1])
# print(sushi_array, sushi_kind)

now_kind = 0
kiso = 0
can_remove = []
for sushi in sushi_array[:K]:
    kiso += sushi[1]
    if sushi_count[sushi[0]] == 0:
        now_kind += 1
        sushi_count[sushi[0]] = 1
    else:
        can_remove.append(sushi[1])

    # print(sushi_count)
ans = kiso + now_kind * now_kind

add_index = K
remove_index = K - 1

# print(ans, kiso, now_kind)
now_kind += 1

for sushi in sushi_array[add_index:]:
    if len(can_remove) == 0 or now_kind > sushi_kind:
        break
    if sushi_count[sushi[0]] == 0:
        kiso += sushi[1] - can_remove.pop()
        sushi_count[sushi[0]] = 1
        # print(ans, kiso, now_kind)
        ans = max(ans, kiso + now_kind * now_kind)
        now_kind += 1
    else:
        continue

print(ans)