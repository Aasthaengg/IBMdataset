A,B=map(int,input().split())
for i in range(10*B,10*(B+1)):
    if A/0.08<=i<(A+1)/0.08:
        print(i)
        x=0
        break
    else:
        x=-1
if x:
    print(x)