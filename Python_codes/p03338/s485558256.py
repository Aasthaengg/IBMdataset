N = int(input())
S = input()
ans = 0
a = [0] * 26
for i in range(N):
    a[ord(S[i])-ord('a')] += 1

b = [0] * 26
for i in range(N):
    a[ord(S[i])-ord('a')] -= 1
    b[ord(S[i])-ord('a')] += 1
    cnt = 0
    for j in range(26):
        if a[j]*b[j]>0:
            cnt += 1
    ans = max(ans,cnt)
print(ans)
