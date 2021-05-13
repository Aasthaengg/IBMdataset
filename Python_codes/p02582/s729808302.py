S = input()

flag = False
ans = 0
for i in range(len(S)):
    if S[i] == 'R':
        ans += 1
        flag = True
    elif S[i] == 'S' and flag:
        break

print(ans)
