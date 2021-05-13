N,A,B=map(int,input().split())
a=0
i=1
while i<=N:
    b=list(str(i))
    for j in range(len(b)):
        b[j]=int(b[j])
    if A<=sum(b) and sum(b)<=B:
        a+=i
    i+=1
print(a)