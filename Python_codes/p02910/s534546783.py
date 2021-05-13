s = input()
ans = 'Yes'
for index, value in enumerate(s):
    if (index + 1)%2 == 0 and value not in ['L', 'U', 'D']:
        ans = 'No'
    elif (index + 1)%2 != 0 and value not in ['R', 'U', 'D']:
        ans = 'No'
        
print(ans)