S=list(str(input()))
x="abcdefghijklmnopqrstuvwxyz"
ans="None"
for i in range(len(x)):
    if x[i] not in S:
        ans=x[i]
        break
print(ans)