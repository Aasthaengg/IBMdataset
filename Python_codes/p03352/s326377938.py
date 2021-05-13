x=int(input())
ans=[1]
for i in range(1,x+1):
    for j in range(2,35):
        if i**j<=x:
            ans.append(i**j)
#print(ans)
print(max(ans))