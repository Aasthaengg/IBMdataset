S=list(input())
ans=700
for i in S: ans += 100 if i == 'o' else 0
print(ans)