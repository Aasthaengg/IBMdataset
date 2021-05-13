a,b=map(int,input().split())
cnt=0
for i in range(a,b+1):
    if all(str(i)[j]==str(i)[len(str(i))-1-j] for j in range(len(str(i))//2))==True:
            cnt+=1
print(cnt)