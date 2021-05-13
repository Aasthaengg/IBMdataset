s = input()
if len(s)%2 == 1:
    s_0 = s[0:(len(s)//2)+1]
    m = s[::-1]
    s_1 = m[0:(len(s)//2)+1]
    
else:
    s_0 = s[0:(len(s)//2)]
    m = s[::-1]
    s_1 = m[0:(len(s)//2)]

ans = 0

for i in range(len(s_1)):
    if s_1[i] != s_0[i]:
        ans += 1
print(ans)