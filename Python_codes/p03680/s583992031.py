n=int(input())
data=[]
for i in range(n):
    data.append(int(input()))
ans=0
index=1
for i in range(n):
    ans += 1
    index=data[index-1]
    if index == 2:
        print(ans)
        break
else:
    print(-1)