class Imos_1:
    def __init__(self,N):
        self.len=N
        self.list=[0]*(N+1)

    def Add(self,F,T,C=1):
        self.list[F]+=C
        self.list[T+1]-=C

    def Cumulative_Sum(self):
        Y=[0]*(self.len)
        S=0
        for i in range(self.len):
            S+=self.list[i]
            Y[i]=S

        return Y
#================================================
N,M=map(int,input().split())
I=Imos_1(N)

for _ in range(M):
    a,b=map(int,input().split())
    a,b=min(a,b),max(a,b)
    I.Add(a,b-1,1)

J=I.Cumulative_Sum()

F=True
for k in J:
    F&=not(k%2)

if F:
    print("YES")
else:
    print("NO")

