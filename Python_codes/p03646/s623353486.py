k=int(input())
x=k//50
y=k%50
ans=[x-y+49 for i in range(50)]
for i in range(y):
    ans[i]+=51
print(50)
print(" ".join(map(str,ans)))