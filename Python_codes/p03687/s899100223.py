s=input()
ans=100
for i in [chr(97+i)for i in range(26)]:
    a=b=0
    for j in s:
        if i!=j:
            a+=1
        else:
            a=0
        b=max(b,a)
    ans=min(ans,b)
print(ans)