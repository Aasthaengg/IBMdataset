# A - Dividing a String
S = input()
ans = 0
tmp = ''
prev = ''
for i in range(len(S)):
    tmp += S[i]
    if tmp!=prev:
        ans += 1
        prev = tmp
        tmp = ''
print(ans)