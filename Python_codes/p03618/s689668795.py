n=input()
m=len(n)

A={chr(i):0 for i in range(97,97+26)}
B={chr(i):0 for i in range(97,97+26)}

cnt=0
for i in range(m):
    A[n[i]] +=1
for i in range(m):
    B[n[i]] +=1
    cnt +=A[n[i]]-B[n[i]]
print(m*(m-1)//2-cnt+1)