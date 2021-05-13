n = int(input())
s = input()
t = input()
cnt = 0
# for i in range(len(s)):
#     if s[-i-1] == t[i]:
#         #print(s[-i],t[i])
#         cnt += 1
#     else:
#         break
ans = 0
for i in range(len(s)):
    if s[i] == t[cnt]:
        cnt += 1
    elif s[i] != t[cnt] and s[i] == t[0]:
        ans = max(ans,cnt)
        cnt = 1
    else:
        ans = max(ans,cnt)
        cnt = 0
print(n + n - cnt)
