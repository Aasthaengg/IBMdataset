N=int(input())
x=N//4
ans="No"
for i in range(x+1):
    for j in range(101):
        if 4*i+7*j==N:
            ans="Yes"
print(ans)