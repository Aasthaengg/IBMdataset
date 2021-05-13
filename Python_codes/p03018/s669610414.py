s = input()

t = s.replace('BC', 'X')

# parts = []
# i_prev = 0
# for i in range(1, len(t) + 1):
#     if t[i] in 'BC':
#         parts.append(t[i_prev : i])
#         i_prev = i + 1
#     else:
#         continue
# else:
#     if i_prev < N: parts.append(t[i_prev : N])
parts = t.replace('B', 'C').split('C')

ans = 0
for part in parts:
    cnt_A = 0
    for i in range(len(part)):
        if part[i] == 'A':
            cnt_A += 1
        else:
            ans += cnt_A

print(ans)