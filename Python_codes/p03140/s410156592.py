n=int(input())
ans=[0]*n

s=[]
for i in range(3):
    s.append(list(input()))

for i in range(n):
    if s[0][i]==s[1][i] and s[1][i]==s[2][i]:
        ans[i]=0
    elif s[0][i]==s[1][i] or s[0][i]==s[2][i] or s[1][i]==s[2][i]:
        ans[i]=1
    else:
        ans[i]=2

print(sum(ans))