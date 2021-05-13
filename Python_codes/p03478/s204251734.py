N,A,B = map(int,input().split())
T=[]
for i in range(1,N+1):
    t=str(i)
    count=0
    for j in range(len(t)):
        count += int(t[j])
    if A <= count <= B:
        T.append(i)
print(sum(T))

