s=input()
result=[]
ans='yes'
for i in s:
    if i in result:
        ans='no'
    result.append(i)
print(ans)
