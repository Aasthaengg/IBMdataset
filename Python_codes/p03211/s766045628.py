s=input()
ans=753
for i in range(0,len(s)-3+1):
    ans=min(abs(int(s[i:i+3])-753),ans)
print(ans)