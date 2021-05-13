N=str(input())
x=0
ans="No"
for i in range(10):
    if N.count(str(i))>=3:
        if int(N[1])==i and int(N[2])==i:
            ans="Yes"
            break
        else:
            break
print(ans)