s=input()
count=1
ans='Yes'
for i in s:
    if count%2==1:
        if i=='R' or i=='U' or i=='D':
            count+=1
            continue
        else:
            ans='No'
            break
    else:
        if i=='L' or i=='U' or i=='D':
            count+=1
            continue
        else:
            ans='No'
            break
print(ans)
