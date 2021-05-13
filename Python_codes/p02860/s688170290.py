n = int(input())
s = input()


ans="Yes"
for i in range(len(s)//2):
    if s[i]!=s[i+len(s)//2]:
        ans="No"
        break

if len(s)%2!=0:
    ans="No"
print(ans)
