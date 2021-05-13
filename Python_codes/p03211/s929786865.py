s=list(input())
ans=[]
for i in range(len(s)-2):
    ans.append(abs(int(''.join(s[i:i+3]))-753))
print(min(ans))