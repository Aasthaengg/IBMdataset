S = input()
S_len = len(S)
S_list = list(S)
ans = ''

if S_len == 2:
    print(S)

elif S_len == 3:
    for i in range(S_len-1, -1, -1):
        ans += S_list[i]
    print(ans)