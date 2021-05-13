T = input()
# pt = ''
# cnt = 0
# for t in T:
#     if t == 'D':
#         cnt += 1 + (pt == 'P')
#     elif t == '?':
#         cnt += 1 + (pt == 'P')
#     pt = t

# print(cnt)
ans = []
for t in T:
    if t == '?':
        ans.append('D')
    else:
        ans.append(t)
print(''.join(ans))
