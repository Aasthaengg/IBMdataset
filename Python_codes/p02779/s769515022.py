n=int(input())
table=sorted(list(map(int,input().split())))
for i in range(n-1):
    if table[i]==table[i+1]:
        print("NO")
        exit()
print("YES")
