def comb(n,k): #nCkを出力する関数
    ans = [[1]]
    tem = []
    for i in range(1,n+1):
        tem = []
        for j in range(i+1):
            if(j==0 or j==i):
                tem.append(1)
            else:
                tem.append(ans[i-1][j-1]+ans[i-1][j])
        ans.append(tem)
    return ans[n][k] 

n,a,b = map(int,input().split())
v = list(map(int,input().split()))
v.sort(reverse = True)
sum = 0
for i in range(a):
    sum+=v[i]
print(sum/a)
count = v.count(v[0])
if count<a:
    count = v.count(v[a-1])
    check = 0
    for i in range(a,n):
        if v[i]!=v[a-1]:
            break
        check+=1
    print(comb(count,check))
else:
    ans = 0
    for i in range(a,min(b+1,count+1)):
        ans += comb(count,i)
    print(ans)

