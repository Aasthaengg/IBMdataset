n, k = map(int, input().split())
s = input()
hand_list = []
for i in range(n):
    if i == 0:
        hand_list.append(i)
    else:
        if s[i] != s[i - 1]:
            hand_list.append(i)
hand_list.append(n)

ans_list = []
if len(hand_list) > 2 * k:
    for i in range(len(hand_list) - 2 * k):
        if s[hand_list[i]] == '1':
            ans = hand_list[min(i + 2 * k + 1, len(hand_list)-1)] - hand_list[i]
        else:
            ans = hand_list[i + 2 * k] - hand_list[i]
        ans_list.append(ans)
else:
    ans_list.append(n)
print(max(ans_list))