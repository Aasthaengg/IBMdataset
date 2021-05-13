n=int(input())
for i in range(1,1000):
    if i*(i+1)==n*2:
        print("Yes")
        k=i+1
        print(k)
        break
else:
    print("No")
    quit()
ans=[[0]*(k-1) for i in range(k)]
x=1
for i in range(k-1,0,-1):
    for j in range(i):
        ans[-i-1][-j-1]=x
        ans[-i+j][-i]=x
        x+=1
for i in ans:
    print(k-1," ".join(map(str,i)))