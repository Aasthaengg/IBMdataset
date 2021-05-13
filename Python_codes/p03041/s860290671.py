n,k=map(int,input().split())
s=input()
result=''
for i in range(n):
    if i==k-1:
        p=str(s[i]).lower()
        result+=p
    else:
        result+=s[i]
print(result)