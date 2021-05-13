a,b=map(int,input().split())
ans=[]
for i in range(100):
    if i<50:
        ans.append(["#"]*100)
    else:
        ans.append(["."]*100)

for i in range(0,49,2):
    for j in range(0,100,2):
        if a==1:
            break
        ans[i][j]="."
        a-=1
    if a==1:
        break

for i in range(51,100,2):
    for j in range(0,100,2):
        if b==1:
            break
        ans[i][j]="#"
        b-=1
    if b==1:
        break
print(100,100)
for i in ans:
    print("".join(i))