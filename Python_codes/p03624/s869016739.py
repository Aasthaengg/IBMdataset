# B - Not Found
S = input()
c = [0]*27
for i in range(len(S)):
    c[ord(S[i])-ord('a')] = 1
i = 0
while c[i]:
    i += 1
ans = chr(ord('a')+i) if i<26 else 'None'
print(ans)