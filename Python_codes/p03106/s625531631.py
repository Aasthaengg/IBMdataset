A,B,K=map(int,input().split())
lst=[]
a=min(A,B)
for i in range(1,a+1):
    if A%i==0:
        if B%i==0:
            lst.append(i)
lst.reverse()
print(lst[K-1])