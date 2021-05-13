n,k =map(int,input().split())
s =str(input())
ans = []
for i in range(n):
    if i == k-1:
        ans.append(s[i].lower())
        
    else:
        ans.append(s[i])

print(''.join(ans))
