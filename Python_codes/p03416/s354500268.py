A,B=map(int,input().split())
ans=0
for i in range(A,B+1):
    temp=""
    tamp=i
    for j in range(len(str(i))):
        temp+=str(i%10)
        i=i//10
    if str(tamp)==temp:
        ans+=1
print(ans)
