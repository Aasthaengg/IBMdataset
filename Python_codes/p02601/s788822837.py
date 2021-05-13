A,B,C=map(int,input().split())
K=int(input())

if A<B<C:
    print("Yes")
    exit()
else:
    for k in range(1,K+1):
        for i in range(3**k):
            a,b,c=A,B,C
            for _ in range(k):
                if i%3==0:
                    a*=2
                elif i%3==1:
                    b*=2
                else:
                    c*=2
                i//=3
            if a<b<c:
                print("Yes")
                exit()
print("No")