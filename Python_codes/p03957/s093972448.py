s = input()
n = len(s)
ans = 'No'
for i in range(n):
    for j in range(i+1,n):
        if s[i] == 'C' and s[j] == 'F':
            ans = 'Yes'
            break
print(ans)