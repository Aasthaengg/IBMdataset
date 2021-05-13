n = int(input())
s = input()
cnt = 0
ans = 0

for i in s:
    if i == 'I':
        cnt += 1
    else:
        cnt -= 1
    
    ans = max(ans,cnt)
    
print(ans)