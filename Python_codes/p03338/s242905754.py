n = int(input())
s = input()
ans = 0

for i in range(1,n):
    s1 = s[:i]
    s2 = s[i:]
    S1 = list(set(s1))
    cnt = 0
    for j in range(len(S1)):
        if S1[j] in s2:
            cnt += 1
            ans = max(ans, cnt)
            
print(ans)