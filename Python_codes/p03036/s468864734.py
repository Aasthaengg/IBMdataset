a,b,c=map(int,input().split())
ans=[c]
for i in range(10):
    ans.append(ans[i]*a-b)
    print(ans[i+1])