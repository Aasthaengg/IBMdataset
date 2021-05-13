A=sorted(list(map(int,input().split())))
a=A[0]
b=A[1]
if (b-a)%2==0:
    print(a+(b-a)//2)
else:
    print("IMPOSSIBLE")