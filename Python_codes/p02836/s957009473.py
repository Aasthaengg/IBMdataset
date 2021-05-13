S_list = list(input())

ans = 0

for i in range(len(S_list) // 2):
    if S_list[i] != S_list[-i - 1]:
        ans += 1

print(ans)
