X,A=map(int,input().split())

if 0<=X<=9 and 0<=A<=9:
    if X<A:
        print(0)
    elif X>=A:
        print(10)
else:
    pass