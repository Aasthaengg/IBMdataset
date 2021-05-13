l = list(map(int,input().split()))
ans = []
for i in range(2) :
    for j in range(i+1,3) :
        ans.append(l[i]+l[j])
print(min(ans))
