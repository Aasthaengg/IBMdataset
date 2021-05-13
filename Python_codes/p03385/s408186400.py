S = input()
ans = 'Yes'
if S[0] == S[1]:
    ans = 'No'
if S[0] == S[2]:
    ans = 'No'
if S[1] == S[2]:
    ans = 'No'
print(ans)    
