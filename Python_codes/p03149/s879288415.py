n=sorted(list(map(int,input().split())))
a=[1,4,7,9]
for i in range(4):
    if a[i]!=n[i]:
        print("NO")
        exit()
print("YES")
