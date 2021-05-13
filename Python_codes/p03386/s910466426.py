a,b,k=map(int,input().split())
if k<=(b-a+1)//2:
    A=set()
    for i in range(k):
        A.add(a+i)
        A.add(b-i)
    print(*sorted(A),sep="\n")
else:
    for i in range(a,b+1):
        print(i)