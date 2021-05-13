N=int(input())
n=0
for i in range(1,N+1):
    list1=list(str(i))
    #print(list1)
    #print(len(list1))
    if len(list1)%2 != 0:
        n+=1
print(n)
