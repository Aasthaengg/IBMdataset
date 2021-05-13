s = list(input())

ans=[]
for i in s[::2]:
    ans.append(i)
Str = "".join(ans)
print(Str)