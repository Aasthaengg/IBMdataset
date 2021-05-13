N=int(input())
if N==1:
    print("Yes")
    print(2)
    print(1,"",1)
    print(1,"",1)
    quit()
find=False
for i in range(2,N+1):
    if i*(i-1)==2*N:
        find=True
        k=i
        break
if not find:
    print("No")
    quit()
S=2*N//k


list=[[] for i in range(k)]
par1=0
par2=1
for _ in range(k-1):
    num=S-len(list[par1])
    for j in range(num):
        list[par1].append(par2+j)
    for i in range(S-par1):
        list[par1+1+i].append(par2+i)
    #print("WW",list)
    par2+=S-par1
    par1+=1
print("Yes")
print(k)
for i in range(k):
    print(str(S)+" "+" ".join(map(str,list[i])))
