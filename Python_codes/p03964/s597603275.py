N = int(input())
T,A = map(int,input().split())
for i in range(N-1):
    t,a = map(int,input().split())
    pro = max((T+t-1)//t,(A+a-1)//a)
    T = t*pro
    A = a*pro
print(T+A)