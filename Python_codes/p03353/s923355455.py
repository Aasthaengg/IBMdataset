s=input()
 
n=int(input())
 
ans = []
 
for i in range(len(s)):
    for j in range(1,7):
        if s[i:i+j] not in ans and j <= len(s):
            ans.append(s[i:i+j])
ans.sort()
#print(ans)
print(ans[n-1])