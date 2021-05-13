s = input()
s_array = list(set(s))
if len(s_array) == 1:
    print(0)
    exit()

ans = float('inf')
s_len = len(s)
for target in s_array:
    s_check = s
    for i in range(1,s_len):
        count = 0
        s_dosh = [""] * (s_len-i)
        for j in range(s_len-i):
            if s_check[j] == target or s_check[j+1] == target:
                s_dosh[j] = target
            else:
                s_dosh[j] = s[j]
                count = 1
        s_check = ''.join(s_dosh)
        # print(s_check)
        if count == 0:
            ans = min(ans,i)
            break

print(ans)