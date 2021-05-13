n,k = map(int,input().split())
l = list(input())

ans = 0

check =[[0]]
i = 0
while i < n:
    if l[i] == "1":
        a = i
        while i < n and l[i] == "1":
            i += 1
        check.append([a,i-1])
    i += 1
check.append([n-1])
if len(check)-k < 1:
    print(n)
    exit()
for i in range(len(check)-k):
       
    ans = max(ans,check[i+k][-1]-check[i][0]+1)
print(ans)

