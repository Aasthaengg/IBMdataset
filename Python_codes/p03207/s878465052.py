n=int(input())
ans=[]
for i in range(n):
    ans.append(int(input()))
ans=sorted(ans)
ans[-1]//=2
print(sum(ans))