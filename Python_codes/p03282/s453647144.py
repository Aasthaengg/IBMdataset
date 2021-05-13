s = list(map(int, list(input())))
k = int(input())
ans = 1

if len(s) <= k:
    for i in s:
        if i != 1:
            ans = i
            break
else:
    for i in range(0,k):
        if s[i] != 1:
            ans = s[i]
            break

print(ans)
