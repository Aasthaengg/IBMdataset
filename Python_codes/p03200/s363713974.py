S = input()
ans = 0
x = 0
for i in range(len(S)):
    if S[i] == 'B':
        x += 1
    else:
        ans += x
print(ans)


