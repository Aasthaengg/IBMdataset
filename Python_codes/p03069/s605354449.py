n = int(input())
s = list(input())
b_c,w_c = s.count('#'),s.count('.')
ans = w_c
b_r,w_r = 0,0
for i in range(n-1):
    if s[i]=='#':b_r+=1
    else:w_r+=1
    if s[i]!=s[i+1]:
        ans = min(ans,b_r+w_c-w_r)
if s[-1]=='#':b_r+=1
else:w_r+=1
ans = min(ans,b_r+w_c-w_r)
print(ans)