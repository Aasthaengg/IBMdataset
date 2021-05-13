a,b=map(int,input().split())
ans=[[] for _ in range(100)]
for i in range(100):
    for j in range(100):
        if i<=49:
            ans[i].append(".")
        else:
            ans[i].append("#")
a-=1
b-=1
for i in range(0,50,2):
    for j in range(0,100,2):
        if b>0:
            ans[i][j]="#"
            b-=1
for i in range(51,100,2):
    for j in range(0,100,2):
        if a>0:
            ans[i][j]="."
            a-=1
print(100,100)
for i in range(100):
    print("".join(ans[i]))