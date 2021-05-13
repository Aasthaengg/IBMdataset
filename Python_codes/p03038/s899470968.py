N, M = map(int, input().split())
A_LIST = list(map(int, input().split()))
BC_LIST = []
for i in range(M):
    b, c = map(int, input().split())
    BC_LIST.append([b, c])
card_dict = {}
for a in A_LIST:
    if a in card_dict:
        card_dict[a] += 1
    else:
        card_dict[a] = 1
for b, c in BC_LIST:
    if c in card_dict:
        card_dict[c] += b
    else:
        card_dict[c] = b
card_list = sorted(card_dict.items(), reverse=True, key=lambda x: x[0])
ans = 0
remaining = N
for num, cnt in card_list:
    ans += num * min(cnt, remaining)
    remaining -= min(cnt, remaining)
    if remaining == 0:
        break
print(ans)
