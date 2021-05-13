S=input()
w=int(input())
ans=''
for i,s in enumerate(S):
    if not i%w:
        ans+=s
print(ans)