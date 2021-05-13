S  = input()
ans = ''
for i in range((len(S)+1)//2):
    ans += S[2*i]
print(ans)