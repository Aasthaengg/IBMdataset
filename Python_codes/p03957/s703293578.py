s=list(input())
n=len(s)
ans="No"
for i in range(n):
    if(s[i]=="C"):
        for j in range(n-i-1):
            if(s[i+j+1]=="F"):
                ans="Yes"
print(ans)