A,B,K=map(int,input().split())
i=0
while i<K:
    if i%2:
        B=B//2*2
        A,B=A+B//2,B//2
    else:
        A=A//2*2
        A,B=A//2,B+A//2
    i+=1
print(A,B)