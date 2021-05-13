n=int(input())

#Sはn以上になる
#単純グラフのため、末端は一つとしか接続しない点がでてくる
#つまりsはn以下
#Sはnとしてよい

tree=[[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i!=j:
            tree[i].append(j)

ans=[]
if n%2==0:
    for i in range(n):
        for item in tree[i]:
            if item+1!=n-i:
                if i>item:
                    ans.append([i+1,item+1])

else:
    for i in range(n):
        if i==n-1:
            for item in tree[i]:
                if i>item:
                    ans.append([i+1,item+1])
        else:
            for item in tree[i]:
                if item+1!=n-(i+1):
                    if i>item:
                        ans.append([i+1,item+1])

print(len(ans))
for item in ans:
    print(item[0],item[1])




