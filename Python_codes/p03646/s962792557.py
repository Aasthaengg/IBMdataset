K=int(input())
print(50)
ans=[i for i in range(51)]
ans.pop(50-K%50)
res=''
for i in range(50):
    res+=str(K//50+ans[i])+' '
print(res[:-1])