n = int(input())
l = list(map(int,input().split()))
ans = 0
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            if l[i] != l[j] and l[j] != l[k] and l[k] != l[i] and 2 * max(l[i],l[j],l[k]) < l[i]+l[j]+l[k]:
                ans += 1
print(ans)