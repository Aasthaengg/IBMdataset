s = str(input())
n = len(s)
ans = []
for i in range(n):
    if i%2 == 0:
        ans.append(s[i])
print(''.join(ans))
