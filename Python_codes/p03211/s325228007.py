s=input()
s_length=len(s)
target=753
ans=753
for i in range(s_length-2):
    comp=int(s[i:i+3])
    ans=min(abs(target-comp),ans)
print(ans)