n=int(input())


count=len(str(n))
ans=''
if count%2==0:
    for i in range(count-1):
        if i%2==0:
            ans+='9'
        else:
            ans+='0'
else:
    ans=(count//2)*'90'
    try:
        ans=n-int(ans)
    except:
        ans=n
print(int(ans))
