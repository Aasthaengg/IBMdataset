a,b,k = map(int,input().split())
A=[]
B=[]
for i in range(a,min(a+k,b+1)):
    A.append(i)
for j in range(b,max(b-k,a-1),-1):
    A.append(j)
B=list(set(A))
B.sort(reverse=False)
for p in range(len(B)):
    print(B[p])