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
for sushi in sushi_array[:K]:
    kiso += sushi[1]
    if sushi_count[sushi[0]] == 0:
        now_kind += 1
    sushi_count[sushi[0]] += 1

ans = kiso + now_kind * now_kind

add_index = K
remove_index = K - 1

now_kind += 1
while now_kind <= sushi_kind:

    while add_index < N:
        sushi = sushi_array[add_index]
        # print(sushi)
        add_index += 1
        if sushi_count[sushi[0]] == 0:
            kiso += sushi[1]
            sushi_count[sushi[0]] = 1
            break

    else:
        break
    while remove_index >= 0:
        sushi = sushi_array[remove_index]
        # print(sushi)
        remove_index -= 1
        if sushi_count[sushi[0]] > 1:
            kiso -= sushi[1]
            sushi_count[sushi[0]] -= 1
            break
    else:
        break
    # print(ans,kiso,now_kind * now_kind)
    ans = max(ans, kiso + now_kind * now_kind)
    now_kind += 1

print(ans)