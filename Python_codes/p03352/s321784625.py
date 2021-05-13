x = int(input())
ans = 1
for i in range(1,x):
    for j in range(2,50):
        if i**j<=x:
            ans = max(ans,i**j)
        else:
            break
    if i**2>x:
        break
print(ans)