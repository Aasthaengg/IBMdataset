N=int(input())
ls1=[]
for i in range(N):
    si,pi=input().split()
    pi2=int(pi)
    ls2=[si,pi2,i+1]
    ls1.append(ls2)
ls1.sort(key=lambda x:-x[1])   
ls1.sort(key=lambda x:x[0])
for i in range(N):
    print(ls1[i][2])