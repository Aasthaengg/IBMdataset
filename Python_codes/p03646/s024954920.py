K=int(input())
print(50)
a=[K//50+i for i in range(49,-1,-1)]
for i in range(K%50):
    a[i]+=1
print(*a)