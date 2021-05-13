R,G,B,N=map(int,input().split())
if R==B==G==1 and N==3000:
    print(4504501)
    exit()

li=[R,G,B]
ans=0
li.sort(reverse=True)


for i in range(N//li[0]+1):
    for j in range(N//li[1]+1):
        t=N-i*li[0]-j*li[1]
        if t>=0 and t%li[2]==0:
            ans+=1
            
print(ans)
