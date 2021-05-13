a, b= [input() for i in range(2)]
ans = 0;
for i in range(3):
    if a[i]==b[i]:
        ans+=1
print(ans)