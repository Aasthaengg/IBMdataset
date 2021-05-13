A,B,C=map(int,input().split())
a=0
for i in range(10**3):
    if A%2==0 and B%2==0 and C%2==0:
        a+=1
        A,B,C=(B+C)//2,(A+C)//2,(A+B)//2
    else:
        print(a)
        break
else:
    print(-1)
