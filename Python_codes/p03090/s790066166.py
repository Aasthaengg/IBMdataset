N=int(input())

if N%2==0:
    S=N+1
else:
    S=N

ans=[]

for i in range(1,N+1):
    for j in range(i+1,N+1):
        if not i+j==S:
            ans.append([i,j])
print(len(ans))
for a,b in ans:
    print(a,b)
