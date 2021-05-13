s = input()
ans = 'No'
index = s.find(s[0], 1)
if index >= 1:
    s = s.replace(s[0], '')
    if (len(s) == 2):
        if (s[0] == s[1]):
            ans ='Yes'
    
print(ans)