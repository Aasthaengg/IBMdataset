n=int(input())
a=[int(x) for x in input().split()]
b=[]
for i in range(n):
    if a[i]==i+1:continue
    if a[a[i]-1]==i+1:
        t=[a[i]-1,i]
        b.append(sorted(t))
# print(b)
print(len(b)//2)