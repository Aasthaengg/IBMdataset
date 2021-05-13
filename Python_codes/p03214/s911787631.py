n=int(input())
a=list(map(int,input().split()))
ave=(sum(a)/len(a))
#print(ave)
li=[]

for i in range(n):
    li.append(abs(ave-a[i]))
    
print(li.index(min(li)))