s = str(input())
n = len(s)
z = 'Yes'
for i in range(n//2):
    if s[i] != s[-1-i]:
        z = 'No'
if z == 'Yes':
    for h in range(len(s[:(n-1)//2])):
        if s[:(n-1)//2][h] != s[:(n-1)//2][-1-h]:
            z = 'No'
            break
if z == 'Yes':
    for j in range(len(s[((n+3)//2)-1:])):
        if s[((n+3)//2)-1:][j] != s[((n+3)//2)-1:][-1-j]:
            z = 'No'
            break
print(z)